from warnings import warn

class Chart:
    def __init__(self, len:int=0,rows:list[str]=[]) -> None:
        self.len = len
        self.content = {}
        for r in rows:
            self.add_row(r)

    def __getitem__(self,arg:any):
        if type(arg) == str:
            return self.access_by_row(arg)
        elif type(arg) == int:
            return self.access_by_index(arg)
        elif type(arg) == tuple and len(arg) == 2:
            if not (type(arg[0]) == str and type(arg[1]) == int):
                raise ValueError('Should be str and int when there are two arguments!')
            return self.access_by_row_and_index(arg[0],arg[1])
        else:
            raise ValueError('Invalid indexer!')
        
    def __setitem__(self,arg:any,value):
        if type(arg) == str:
            return self.update_by_row(arg,value)
        elif type(arg) == int:
            return self.update_by_index(arg,value)
        elif type(arg) == tuple and len(arg) == 2:
            if not (type(arg[0]) == str and type(arg[1]) == int):
                raise ValueError('Should be str and int when there are two arguments!')
            return self.update_by_row_and_index(arg[0],arg[1],value)
        else:
            raise ValueError('Invalid indexer!')

    def add_row(self, row:str) -> None:
        if type(row) != str:
            raise ValueError('Row name should be str type, not %s'%(type(row)))
        if row in self.content.keys():
            return
        self.content[row] = [None for i in range(self.len)]

    def update_by_row(self, row:str, value:list[any]) -> None:
        if self.len != len(value):
            raise ValueError('list len should be equal to %d, not %d'%(self.len,len(value)))
        self.content[row] = value

    def update_by_index(self, index:int, value:dict[any]) -> None:
        if not set(value.keys()).issubset(set(self.content.keys())):
            raise ValueError('dict keys should be a subset of chart keys!')
        for k in value.keys():
            self.content[k][index] = value[k]

    def update_by_row_and_index(self, row:str, index:int, value:any) -> None:
        try:
            self.content[row][index] = value    
        except:
            raise ValueError('Update value fail!')

    

    def access_by_row(self, row:str) -> list[any]:
        try:
            return self.content[row]
        except:
            raise ValueError('Access by row %s fail!'%(row))

    def access_by_index(self, index:int) -> dict[any]:
        try:
            res = {}
            for k in self.content.keys():
                res[k] = self.content[k][index]
            return res
        except:
            raise ValueError('Access by index %d fail!'%(index))

    def access_by_row_and_index(self, row:str, index:int) -> any:
        try:
            return self.content[row][index]
        except:
            raise ValueError('Access by row %s and index %d fail!'%(row,index))
        


    