from create_slideshow import *

def calc_score(photo1, photo2):
    tags1 = sorted(photo1.tags)
    tags2 = sorted(photo2.tags)
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
        if i > len(tags1):
            done = True
            distinct2 += len(tags2)-j
        if j > len(tags2):
            done = True
            distinct1 += len(tags1)-i
        
            
        
    return matching+distinct1+distinct2

def take_best(start, vals):
    return None
