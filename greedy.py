from create_slideshow import *
import numpy as np
from collections import deque

def calc_score(slide1, slide2):
    tags1 = slide1.tags
    tags2 = slide2.tags
    i =0
    j = 0
    matching = 0
    distinct1 =0
    distinct2 = 0
    done = False
    while not done:
        if tags1[i] == tags2[j]:
            matching+=1
            i+=1
            j+=1
        elif tags1[i] < tags2[j]:
            distinct1+=1
            i+=1
        else:
            distinct2+=1
            j+=1
        if i >= len(tags1):
            done = True
            distinct2 += len(tags2)-j
        if j >= len(tags2):
            done = True
            distinct1 += len(tags1)-i
        
            
        
    return min([matching,distinct1,distinct2])

def take_best(start, slides,num = 1000):
    tmp = slides.pop()
    i = tmp[0]
    s = tmp[1]
    best_score = calc_score(start,s)
    best_index = i
    best_slide = s
    crap_slides = deque([],maxlen=len(slides)-1)
    while((len(crap_slides)<num) & (len(slides)>0)):
        tmp = slides.pop()
        i = tmp[0]
        s = tmp[1]
        score = calc_score(start,s)
        if score>best_score:
            crap_slides.append((best_index,best_slide))
            best_score = score
            best_slide = s
            best_index = i

        else:
            crap_slides.append((i,s))
    crap_slides.extend(slides)
    return best_index,best_slide,crap_slides

def do_greedy(slides,block_size = 100):
    blocks = [deque([(n*block_size+i,j) 
                     for i,j in enumerate(slides[n*block_size:(n+1)*block_size])
                    ]) 
              for n in range(len(slides)//block_size)
             ]
    order = deque([],maxlen=len(slides))
    for to_process in blocks:
        tmp = to_process.pop()
        order.append(tmp[0])
        curr = tmp[1]
        while(len(to_process) > 1):
            i,s,p = take_best(curr,to_process,block_size)
            order.append(i)
            curr = s
            to_process = p

    out = []
    while(len(order)>0):
        out+=[slides[order.popleft()]]
    print(out[:10])
    
    return out


