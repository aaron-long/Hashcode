from create_slideshow import Photo


def read_input(filename):

    with open(filename,'r') as f:
        size = int(f.readline())
        pics = [Photo()]*size
        i = 0
        for line in f.readlines():
            tokens = line.split()
            orientation = tokens[0]
            tags = tokens[2:]
            pics[i] = Photo(orientation, i, tags)
            i += 1
    return pics


def write_output(filename, photos):

    terminator = '\n'
    with open(filename, 'w') as f:
        size = len(photos)
        f.write(str(size) + terminator)

        for photo in photos:
            f.write(str(photo.num) + terminator)

