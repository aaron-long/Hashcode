from create_slideshow import *

def calc_score(slide1, slide2):
    tags1 = sorted(slide1.tags)
    tags2 = sorted(slide2.tags)
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

def take_best(start, slides):
    best_score = 0
    index = 0
    crap_slides = []
    for tmp in slides:
        i = tmp[0]
        s = tmp[1]
        score = calc_score(start,s)
        if score>best_score:
            crap_slides+=[slides[index]]
            best_score = score
            index = i

        else:
            crap_slides +=[i]
    return index,crap_slides

def do_greedy(slides):
    to_process = list(enumerate(slides))
    order = [slides[0]]
    while(to_process != []):
        i,s = take_best(to_process[0][1],to_process[1:])
        order+=[i]
        to_process = s

    out = []
    for i in order:
        out+=[slides[i]]
    return out

    
