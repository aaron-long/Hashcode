from file_handler import read_input, write_output
from create_slideshow import sort_photos
from greedy import do_greedy

files = ['a_example.txt', 'b_lovely_landscapes.txt', 'c_memorable_moments.txt',
         'd_pet_pictures.txt', 'e_shiny_selfies.txt']


def main():

    for file in files:
        # Create the slideshow
        pics = read_input(file)

        # Sort photos
        slides = sort_photos(pics)

        #slides = do_greedy(slides)

        # Write the slideshow to file
        write_output(file, slides)


if __name__ == '__main__':
    main()

