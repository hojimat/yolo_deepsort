from collections import deque
import cv2 as cv
import numpy as np
import logging
from helpers import crossed_restricted_zone

logger = logging.getLogger('main')

def basic_setup():
    # Add classes and assign colors to them
    classes = open('weights/coco.names').read().strip().split('\n')
    colors = np.full((len(classes),3), (255,0,0)) # make all objects red
    colors[0,:] = (0,255,255) # make person cyan

    # Give the configuration and weight files for the model and load the network.
    net = cv.dnn.readNetFromDarknet('weights/yolov3.cfg', 'weights/yolov3.weights')
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

    # determine the output layer
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

    return net, classes, colors, ln


def detect_single_frame(frame, restricted_zone, history, net, classes, colors, output_layers):
    """
    THIS CODE COMES FROM THE OFFICIAL OPENCV DOCUMENTATION, NOT LLM!
    Here is the link: https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html
    I adapted the code to make it simpler, removed blobs

    """

    # construct a blob from the image
    blob = cv.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)

                
    cv.polylines(frame,
                 [np.array(restricted_zone, dtype=np.int32).reshape((-1,1,2))],
                 isClosed=True, color=(0,0,255), thickness=2)

    net.setInput(blob)
    outputs = net.forward(output_layers)

    boxes = []
    confidences = []
    classIDs = []
    h, w = frame.shape[:2]

    for output in outputs:
        for detection in output:
            scores = detection[5:] #type:ignore
            classID = np.argmax(scores)
            confidence = scores[classID]
            if classID==0 and confidence > 0.5:
                box = detection[:4] * np.array([w, h, w, h]) #type:ignore
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                box = [x, y, int(width), int(height)]
                boxes.append(box)
                confidences.append(float(confidence))
                classIDs.append(classID)

    indices = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    if len(indices) > 0:
        for i in indices.flatten(): #type:ignore
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in colors[classIDs[i]]]
            cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
            cv.putText(frame, text, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # add the intersection boolean to the 3 second history window
    history.append(crossed_restricted_zone(boxes, restricted_zone))

    if any(history):
        cv.putText(frame, "ALARM!", (50,50), cv.FONT_HERSHEY_PLAIN, 2, (0,0,255), 3, cv.LINE_AA)

    cv.imshow('window', frame)


def detect_video(video_path: str, restricted_zone: list[list[int]]):
    """
    THIS CODE COMES FROM TUTORIAL:
    https://www.geeksforgeeks.org/python/python-opencv-cv2-polylines-method/
    """

    video = cv.VideoCapture(video_path)

    # I check intersection in the last 3 seconds as a rolling window
    # I am thinking of a queue of size 3 seconds * frames per second
    # where I push stuff to the queue and always check if any of the last 3 is "True"
    fps = video.get(cv.CAP_PROP_FPS)
    last_3_seconds = deque(maxlen=3)

    frame_number = 0
    while True:
        ok, frame = video.read()
        if not ok:
            break

        # skip frames to save CPU time
        frame_number += 1
        if frame_number % fps != 0:
            continue


        detect_single_frame(frame, restricted_zone, last_3_seconds, *basic_setup())
        if cv.waitKey(1) & 0xFF == 27:
            break

    video.release()
    cv.destroyAllWindows()
