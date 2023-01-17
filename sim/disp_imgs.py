import numpy as np
import cv2
import matplotlib.pyplot as plt
from itertools import cycle

def highlight_img(img,pixels:list[(int,int)]):
    # highlight the area in the pixels list
    highlight_img = img
    highlight_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img_w = img.shape[0]
    img_h = img.shape[1]
    for (x,y) in pixels:
        if x<0 or y<0 or x >= img_w or y >= img_h:
            continue
        (h,s,v) = img[y,x]
        new_v = 2*v
        highlight_img[y,x] = (h,s,new_v)
    highlight_img = cv2.cvtColor(highlight_img,cv2.COLOR_HSV2BGR)
    return highlight_img

def disp_consecutive_imgs(imgs):
    key = 0
    img_iter = cycle(imgs)
    while key & 0xFF != 27:
        cv2.namedWindow('disp')
        cv2.imshow('disp',next(img_iter))
        key = cv2.waitKey(500)
    cv2.destroyAllWindows() 
    return