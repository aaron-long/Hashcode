from read_input import read_input, write_output
from create_slideshow import Photo


filename = 'test_file.txt'

def main():
    # Create the slideshow
    pics = read_input('a_example.txt')

    # Print the pics object
    print('Pics object:', pics)

    write_output(filename, pics)


if __name__ == '__main__':
    main()

