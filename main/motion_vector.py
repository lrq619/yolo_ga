class MOTIONVECTOR:
    def __init__(self,curid=0,refid=0,curx=0,cury=0,refx=0,refy=0,blockw=0,blockh=0) -> None:
        self.curid:int = curid
        self.refid:int = refid
        self.curx:int = curx
        self.cury:int = cury
        self.refx:int = refx
        self.refy:int = refy
        self.blockw:int = blockw
        self.blockh:int = blockh