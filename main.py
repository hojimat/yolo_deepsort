import logging
import cv2 as cv
from object_detection import detect_video

logging.basicConfig(level=logging.DEBUG)

def main():
    detect_video("inputs/test.mp4")


if __name__ == '__main__':
    main()
