import re

def retrive_num_from_str(string:str)->list[float]:
    arr = re.findall(r"\d+\.?\d*",string)
    res = []
    for s in arr:
        res.append(float(s))
    return res


def sort_str_by_num(strings:list[str])->list[str]:
    # sort str by the last number appeared in it
    d = {}
    for s in strings:
        n = int(retrive_num_from_str(s)[-1])
        d[n] = s
    res = []
    for k in sorted(d.keys()):
        res.append(d[k])
    return res

def get_union_pixels(x0:int,y0:int,w0:int,h0:int,
                     x1:int,y1:int,w1:int,h1:int)->list[any]:
    # get two rectangles union area's pixels positions, return [] if none union
    pixels = []
    if (2 * abs(x0-x1) >= (w0+w1)) or (2 * abs(y0-y1) >= (h0+h1)): # none union
        return pixels
    start_x = int(max(x0-w0/2 , x1-w1/2))
    end_x = int(min(x0+w0/2 , x1+w0/2))

    start_y = int(max(y0-h0/2,y1-h1/2))
    end_y = int(min(y0+h0/2,y1+h1/2))

    for x in range(start_x, end_x):
        for y in range(start_y,end_y):
            pixels.append((x,y))
    return pixels