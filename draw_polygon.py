from pathlib import Path
import json
import cv2 as cv


points = []

def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        points.append({"x": x, "y": y})
        print(f"({x},{y})")

img = cv.imread("inputs/abbey_road.png")
assert img is not None
cv.imshow("first_frame", img)
cv.setMouseCallback("first_frame", click_event)
cv.waitKey(0)
cv.destroyAllWindows()

Path("outputs/polygon.json").write_text(json.dumps(points))
