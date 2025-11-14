import json
from pathlib import Path
import logging
import cv2 as cv
from object_detection import detect_video

logging.basicConfig(level=logging.DEBUG)

def main():
    # Import restricted zone
    restricted_zone = json.loads(Path('outputs/polygon.json').read_text())

    detect_video("inputs/test.mp4", restricted_zone)


if __name__ == '__main__':
    main()
