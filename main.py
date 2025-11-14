import json
from pathlib import Path
from config import setup_logger, parse_args
from zone_setup import draw_polygon
from object_detection import detect_video

def main():
    setup_logger()
    opts = parse_args()
    
    # If user chooses to, they can specify the restricted zone manually from the first frame
    if opts['specify_zone']:
        draw_polygon()

    # Import restricted zone
    restricted_zone = json.loads(Path('outputs/polygon.json').read_text())

    # Run detection
    detect_video("inputs/test.mp4", restricted_zone)


if __name__ == '__main__':
    main()
