from config import WORKING_PATH,GOIS_DIR_PATH
from utils.parse import parse_goi




def test0():
    goi_index = 0
    goi_path = '%s/goi%d'%(GOIS_DIR_PATH,goi_index)
    
    goi = parse_goi(goi_path)
    goi.disp_imgs()
    pass

if __name__ == '__main__':
    test0()