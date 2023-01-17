import os
from torchvision import transforms
import PIL.Image as pil_image
import time
import numpy as np


def reduce_resolution(img,downmag):
    w = img.width
    h = img.height
    down_size = (int(h/downmag),int(w/downmag))
    
    down = transforms.Resize(down_size)
    start = time.time()
    up = transforms.Resize((h,w))
    end = time.time()
    res = down(img)
    res = up(res)
    return res,end-start

def create_low_imgs():
    dir = './neverball_high_train'
    total_dura = 0
    count = 0
    if not os.path.exists(dir):
        os.mkdir(dir)
    for file in os.listdir(dir):
        print('\rProcessing %s'%file,end='',flush=True)
        orig_img = pil_image.open('%s/%s'%(dir,file)).convert('RGB')
        low_img,duration = reduce_resolution(orig_img, 2)
        low_img.save('./neverball_train/%s'%file)
        # print(file)
        total_dura += duration
        count += 1
    return total_dura/count

if __name__ == '__main__':
    create_low_imgs()