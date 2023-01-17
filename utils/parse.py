from math import floor
from main.bdbox import BDBOX
from main.motion_vector import MOTIONVECTOR
from main.goi import GOI
from utils.tools import retrive_num_from_str,sort_str_by_num
from config import ROW_NAMES
import cv2
import os

def parse_img_and_bdbox(img_path,bdbox_path) -> list[BDBOX]:
    img = cv2.imread(img_path)
    bdboxs : list[BDBOX] = []
    img_h = img.shape[0]
    img_w = img.shape[1]
    
    with open(bdbox_path) as f:
        for line in f:
            nums = retrive_num_from_str(line)
            if len(nums) != 5:
                print('Bounding Box Parse Fail! This line format incorrect!')
                continue
            type = nums[0]
            x = floor(nums[1] * img_w)
            y = floor(nums[2] * img_h)
            w = floor(nums[3] * img_w)
            h = floor(nums[4] * img_h)
            # print(x,y,w,h)
            bdboxs.append(BDBOX(type,x,y,w,h))
    return img, bdboxs

def parse_ffmpeg_info(ffmpeginfo_path):
    frame_type_path = '%s/frame_type.txt'%(ffmpeginfo_path)
    motion_vector_path = '%s/MotionVector.txt'%(ffmpeginfo_path)
    frame_types = []
    with open(frame_type_path) as f:
        for line in f:
            type = line.split(': ')[-1][0]
            frame_types.append(type)
    motion_vectors = [[] for i in range(len(frame_types))]
    with open(motion_vector_path) as f:
        for line in f:
            nums = retrive_num_from_str(line)
            curid = int(nums[0])
            if frame_types[curid] != 'B': # Reference frame do not need motion vector
                continue
            refid = int(nums[1])
            curx = int(nums[2])
            cury = int(nums[3])
            refx = int(nums[4])
            refy = int(nums[5])
            blockw = int(nums[6])
            blockh = int(nums[7])
            motion_vector = MOTIONVECTOR(curid,refid,curx,cury,refx,refy,blockw,blockh)
            motion_vectors[curid].append(motion_vector)

    return frame_types, motion_vectors


def parse_goi(goi_path) -> GOI:
    
    ffmpeginfo_path = '%s/ffmpeginfo'%(goi_path)
    bdboxs_dir_path = '%s/bdboxs'%(goi_path)
    imgs_dir_path = '%s/imgs'%(goi_path)


    img_fnames = sort_str_by_num(os.listdir(imgs_dir_path))
    bdboxs_fnames = sort_str_by_num(os.listdir(bdboxs_dir_path))

    if len(img_fnames) != len(bdboxs_fnames):
        raise ValueError('length of goi imgs and bdboxs in %s does not match!'%(goi_path))

    goi = GOI(len(img_fnames),ROW_NAMES)
    for i in range(len(img_fnames)):
        img_fname = img_fnames[i]
        bdbox_fname = bdboxs_fnames[i]

        img_path = '%s/%s'%(imgs_dir_path,img_fname)
        bdbox_path = '%s/%s'%(bdboxs_dir_path,bdbox_fname)
        
        img,bdbox = parse_img_and_bdbox(img_path,bdbox_path)
        goi.chart[i] = {'img':img,'bdbox':bdbox}
    

    frame_types, motion_vectors = parse_ffmpeg_info(ffmpeginfo_path)
    goi.chart['frame_type'] = frame_types
    goi.chart['motion_vector'] = motion_vectors

    return goi