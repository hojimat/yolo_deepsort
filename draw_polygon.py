from pathlib import Path
import json
import cv2 as cv
import logging


def draw_polygon():
    points = []
    def click_event(event, x, y, flags, params):
        if event == cv.EVENT_LBUTTONDOWN:
            points.append((x, y))
            print(f"({x},{y})")
            
    video = cv.VideoCapture('inputs/test.mp4')
    ok, frame = video.read()
    video.release()

    if not ok:
        logging.error("no frame")
        return

    cv.imshow("first_frame", frame)
    cv.setMouseCallback("first_frame", click_event)
    cv.waitKey(0)
    cv.destroyAllWindows()

    Path("outputs/polygon.json").write_text(json.dumps(points))

if __name__=='__main__':
    draw_polygon()
