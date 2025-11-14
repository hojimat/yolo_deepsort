# yolo_deepsort
Test task in computer vision

## To-do list

- [ ] Learn what DeepSORT is - never heard of it before
- [x] Import OpenCV YOLO to detect people from a static frame
    - ignore every other object from COCO - only leave people
    - extract bounding boxes from people
- [x] Write a function that does YOLO object detection from video
    - test it
    - be careful about fps to calculate 3 seconds
- [ ] Write a function that checks if anyone crosses the restricted zone
    - probably, in a separate helper module
    - just coordinate check from JSON file
    - also add helper to write "ALERT" on the frame
- [x] GUI for users to click at points and export them to `restricted_zones.json`
    - polygon/shape
    - if given <3 points, error
- [ ] Finalize stuff (dockerize, check versions, check dependencies)

## Initial plan and limitations

- I don't have dedicated GPU, so will use slower models
- I don't have a strong computer to train stuff, so will use pre-trained OpenCV YOLO
- Most of the code is just using libraries and connecting them (e.g. via JSON) and automating some calculations (e.g. 3 second checks)
- Have to learn DeepSORT

## How to run:
1. First you have to specify the restricted zone using:

```bash
python draw_polygon.py
```
