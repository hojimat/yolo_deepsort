from shapely import Polygon


def box_to_coords(bbox: tuple[int,int,int,int]) -> tuple[tuple[int,int],...]:
    """
    Converts OpenCV styled bounding box to 4 vertex coordinates
    x,y,w,h -> (x,y), (x,y+h), (x+w,y), (x+w,y+h)
    """
    # left,right,top,bottom
    lb = (bbox[0], bbox[1])
    rb = (bbox[0] + bbox[2], bbox[1])
    lt = (bbox[0], bbox[1] + bbox[3])
    rt = (bbox[0] + bbox[2], bbox[1] + bbox[3])

    return (lb, rb, lt, rt)





def crossed_restricted_zone(boxes: list[tuple[int,int,int,int]], area: tuple[tuple[int,int]]) -> bool:
    area_polygon = Polygon(area)
    for box in boxes:
        box_polygon = Polygon(box_to_coords(box))
        if box_polygon.intersects(area_polygon):
            return True

    return False
