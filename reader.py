import os

def split_read(file):
    #file  =  "heimer.pdf"
    size = os.path.getsize(file) 
    with open (file , 'rb')as f:
        st = 100000
        if st > size:
            it = size
        else:
            it = int(size/st)
        cont_list = []
        pos = 0
        
        for i in range(it):
            c = f.read(st)
            pos += st
            f.seek(pos)
            cont_list.append(c)
    return cont_list
