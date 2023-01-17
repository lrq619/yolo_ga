import numpy as np
from math import floor
class BDBOX:
    def __init__(self,t,x,y,w,h) -> None:
        self.type = t
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def split_img_bdboxs(img, bdboxs: list[BDBOX]) -> list[any]:
# input: img: an image; bdboxs: a list of BDBOX
# output: all the pixel positions in the format of (x,y) that are in the bdboxs.     
    pixels_pos = []
    img_h = img.shape[0]
    img_w = img.shape[1]
    for bdbox in bdboxs:
        start_x = floor(bdbox.x - bdbox.w / 2)
        end_x = min(img_w,start_x+bdbox.w)
        start_y = floor(bdbox.y - bdbox.h / 2)
        end_y = min(img_h,start_y+bdbox.h)
        
        for x in range(start_x,end_x):
            for y in range(start_y,end_y):
                pixels_pos.append((x,y))
        pixels_pos = list(set(pixels_pos))        
                
    return pixels_pos
    