from file_handler import read_input, write_output


filename = 'slideshow.txt'


def main():
    # Create the slideshow
    pics = read_input('a_example.txt')

    # Print the pics object
    print('Pics object:', pics)

    write_output(filename, pics)


if __name__ == '__main__':
    main()

