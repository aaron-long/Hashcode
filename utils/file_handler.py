from slide_objects import Photo


def read_photo_collection(filename):
    """
    Read in a collection of photos.

    Args:
        filename (str): Filename to import photo collection from

    Returns:
        photo_collection (list[Photo]): List containing the collection of photos
    """
    with open(filename, 'r') as f:
        size = int(f.readline())
        photo_collection = [Photo()] * size
        i = 0
        for line in f.readlines():
            tokens = line.split()
            orientation = tokens[0]
            tags = tokens[2:]
            photo_collection[i] = Photo(orientation, i, tags)
            i += 1
    return photo_collection


def write_slideshow(filename, slides):
    """
    Write a collection of slides to a file.

    Args:
        filename (str): Filename to write slideshow to
        slides (list[Slide]): Collection of slides to write out to file

    Returns:
        None
    """
    terminator = '\n'

    with open('output_files/out_' + filename, 'w') as f:
        size = len(slides)
        f.write(str(size) + terminator)

        for slide in slides:
            num_str = ''
            for i in slide.num:
                num_str += str(i)+' '
            f.write(num_str + terminator)

    return

