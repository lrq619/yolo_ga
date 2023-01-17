from utils.chart import Chart
from utils.tools import get_union_pixels
from main.bdbox import BDBOX,split_img_bdboxs
from main.motion_vector import MOTIONVECTOR
from sim.disp_imgs import disp_consecutive_imgs,highlight_img

class GOI:
    # group of images-info
    def __init__(self,len,rows) -> None:
        self.chart = Chart(len,rows)
    
    def disp_orig_imgs(self):
        disp_consecutive_imgs(self.chart['img'])

    def get_pixels_in_ref_img(self, refid, refx, refy, w, h):
        bdboxs:list[BDBOX] = self.chart[refid]['bdbox']
        macrox = refx + w/2
        macroy = refy + h/2
        macrow = w
        macroh = h
        pixels = []
        for bdbox in bdboxs:
            p = get_union_pixels(bdbox.x,bdbox.y,bdbox.w,bdbox.h,
                                 macrox, macroy, macrow, macroh)
            pixels = pixels + p
            pixels = list(set(pixels))
        return pixels

    def map_pixels_to_cur_img(self, pixels, movex, movey):
        res = []
        for p in pixels:
            res.append((p[0]+movex,p[1]+movey))
        return res

    def split_img_motionv(self,imgid:int) -> list[any]:
        motion_vectors : list[MOTIONVECTOR] = self.chart[imgid]['motion_vector']
        pixels = []
        for motion_vector in motion_vectors:
            refid = motion_vector.refid
            refx = motion_vector.refx
            refy = motion_vector.refy
            w = motion_vector.blockw
            h = motion_vector.blockh
            ref_p = self.get_pixels_in_ref_img(refid,refx,refy,w,h)
            movex = motion_vector.curx - refx
            movey = motion_vector.cury - refy
            ps = self.map_pixels_to_cur_img(ref_p,movex,movey)
            pixels += ps
            pixels = list(set(pixels))
        return pixels
    
    def split_imgs(self):
        # for reference frame, apply bdboxs on the imgs; for non-reference frame, apply mapping
        for i in range(self.chart.len):
            c = self.chart[i]
            img = c['img']
            bdboxs = c['bdbox']
            frame_type = c['frame_type']
            pixels = []
            if not frame_type == 'B':
                pixels = split_img_bdboxs(img,bdboxs)
            else:
                pixels = self.split_img_motionv(i)
            splited_img = highlight_img(img,pixels)
            r = {'img':img,'bdbox':bdboxs,'splited_pixels':pixels,'splited_img':splited_img}
            self.chart[i] = r
        disp_consecutive_imgs(self.chart['splited_img'])

            
        return
        