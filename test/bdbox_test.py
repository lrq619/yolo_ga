from config import WORKING_PATH
from utils.parse import parse_bounding_boxs
from main.bdbox import split_img_bdboxs
from sim.disp_imgs import disp_highlight_img
import cv2
import numpy
import matplotlib.pyplot as plt

BDBOX_FILE_0 = '%s/txt/bdbox/bus.txt'%(WORKING_PATH)
IMG_FILE_0 = '%s/imgs/bus.jpg'%(WORKING_PATH)

def test0():
    img = cv2.imread(IMG_FILE_0)
    bdboxs = parse_bounding_boxs(BDBOX_FILE_0,img)
    
    pixels = split_img_bdboxs(img,bdboxs)

    disp_highlight_img(img,pixels)

    
    
    pass

if __name__ == '__main__':
    test0()