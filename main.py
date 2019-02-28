from file_handler import read_input, write_output
from create_slideshow import sort_photos
from greedy import do_greedy

input_filename = 'b_lovely_landscapes.txt'
output_filename = 'out_' + input_filename

def main():
    # Create the slideshow
    pics = read_input(input_filename)

    # Print the pics object
    print('Pics object:', pics)

    # Sort photos
    slides = sort_photos(pics)

    #slides = do_greedy(slides)

    # Write the slideshow to file
    write_output(output_filename, slides)


if __name__ == '__main__':
    main()

