from config import WORKING_PATH
from utils.parse import parse_bounding_boxs
from main.bdbox import split_img_bdboxs
from sim.disp_imgs import disp_highlight_img,disp_consecutive_imgs
import cv2
import os
import matplotlib.pyplot as plt


BDBOX_DIR = '%s/goi_dir/goi0/bdboxs'%WORKING_PATH
IMG_DIR = '%s/goi_dir/goi0/imgs'%WORKING_PATH



def test0():
    imgs = []
    for filename in os.listdir(IMG_DIR):
        img = cv2.imread('%s/%s'%(IMG_DIR,filename))
        imgs.append(img)
    disp_consecutive_imgs(imgs)

    pass

def test1():
    imgs = []
    for filename in os.listdir(IMG_DIR):
        img = cv2.imread('%s/%s'%(IMG_DIR,filename))
        
        imgs.append(img)
    disp_consecutive_imgs(imgs)

    pass

if __name__ == '__main__':
    test0()