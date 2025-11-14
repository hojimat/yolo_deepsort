from pathlib import Path
import json
import cv2 as cv
import logging

logger = logging.getLogger('main')

def draw_polygon():
    points = []
            
    video = cv.VideoCapture('inputs/test.mp4')
    ok, frame = video.read()
    video.release()
    if not ok:
        logger.error("no frame")
        return

    def click_event(event, x, y, flags, params):
        if event == cv.EVENT_LBUTTONDOWN:
            points.append((x, y))
            print(f"({x},{y})")
            cv.circle(frame, (x,y), 5, (0,0,255), -1)
            cv.imshow("first_frame", frame)


    cv.imshow("first_frame", frame)
    cv.setMouseCallback("first_frame", click_event)
    cv.waitKey(0)
    cv.destroyAllWindows()

    if len(points) < 3:
        logger.error("Please specify at least 3 points for the restricted zone")
        raise ValueError("Please specify at least 3 points")

    Path("outputs/polygon.json").write_text(json.dumps(points))
