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
- [x] Write a function that checks if anyone crosses the restricted zone
    - probably, in a separate helper module
    - just coordinate check from JSON file
    - also add helper to write "ALERT" on the frame
- [x] GUI for users to click at points and export them to `restricted_zones.json`
    - polygon/shape
    - if given <3 points, error
- [ ] Finalize stuff (dockerize, check versions, check dependencies)

## Initial plan and limitations

- Biggest limitation: time constraints - I am busy in the weekdays, and have other commitments at the weekend.
- I don't have dedicated GPU, so will just use slower pre-trained OpenCV YOLO and will skip frames
- Most of the code is just using libraries and connecting them (e.g. via JSON) and automating some calculations (e.g. 3 second checks)
- Have to learn DeepSORT

## How to run:
0. Install requirements using:
```bash
python -m pip install -r requirements.txt
```
1. Run the video detection
```bash
python main.py
```
or, if you want to specify the zone and run video detection:
```bash
python main.py --specify-zone
```

** IMPORTANT: you need to include a directory `weights/` where you put `yolov3.cfg`, `yolov3.weights`, `coco.names` manually - they are .gitignored due to the large file size. You can download them here: `https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html`**

The working project directory structure must look like this:

```
├── inputs
│   └── test.mp4
├── outputs
│   └── ...
├── weights
│   ├── coco.names
│   ├── yolov3.cfg
│   └── yolov3.weights
├── config.py
├── helpers.py
├── zone_setup.py
├── object_detection.py
├── main.py
├── requirements.txt
└── README.md
```
