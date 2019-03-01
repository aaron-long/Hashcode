from file_handler import read_input, write_output, read_params
from create_slideshow import sort_photos
from greedy import do_greedy
import numpy as np
import time

files = ['a_example.txt', 'b_lovely_landscapes.txt', 'c_memorable_moments.txt',
         'd_pet_pictures.txt', 'e_shiny_selfies.txt']

greed = read_params()


def main():

    for f in files:
        # Create the slideshow
        t = time.time()
        pics = read_input(f,1)
        if pics!=[]:
                np.random.shuffle(pics)
                # Sort photos
                slides = sort_photos(pics)

                slides = do_greedy(slides, greed)
                
                # Write the slideshow to file
                write_output(f, slides)
                
        t = time.time()-t
        print('{} done. ({}mins, {:.3}s)'.format(f,t//60,t%60))

if __name__ == '__main__':
    main()

