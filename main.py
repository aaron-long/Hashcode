from read_input import read_input
from create_slideshow import Photo


def main():
    # Create the slideshow
    pics = read_input('a_example.txt')

    # Print the pics object
    print('Pics object:', pics)


if __name__ == '__main__':
    main()

