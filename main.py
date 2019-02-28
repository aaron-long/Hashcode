from file_handler import read_input, write_output
from create_slideshow import sort_photos

filename = 'slideshow.txt'


def main():
    # Create the slideshow
    pics = read_input('a_example.txt')

    # Print the pics object
    print('Pics object:', pics)

    # Sort photos
    slides = sort_photos(pics)

    # Write the slideshow to file
    write_output(filename, slides)


if __name__ == '__main__':
    main()

