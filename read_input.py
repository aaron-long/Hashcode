import numpy as np

def read_input(filename):

    
    with open(filename,'r') as f:
        size = int(f.readline())
        pics = [0]*size
        i=0
        for line in f.readlines():
            tokens = line.split()
            orientation = tokens[0]
            tags = tokens[2:]
            pics[i]=(orientation,tags)
            i+=1
    return pics
