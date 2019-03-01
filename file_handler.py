from create_slideshow import Photo


def read_params(filename='params.txt'):
    with open(filename, 'r') as f:
        greed = f.readline()
    return greed


def read_input(filename,threshold =1):

    with open(filename, 'r') as f:
        size = int(f.readline())
        print(size)
        pics = [Photo()]*size
        i = 0
        idx = 0
        for line in f.readlines():
            tokens = line.split()
            if int(tokens[1])>threshold:
                orientation = tokens[0]
                tags = tokens[2:]
                pics[i] = Photo(orientation, idx, tags)
                i += 1
            idx+=1
        pics = pics[:i]
        print(i)
    return pics


def write_output(filename, slides):

    terminator = '\n'
    with open('out_' + filename, 'w') as f:
        size = len(slides)
        f.write(str(size) + terminator)

        for slide in slides:
            num_str = ''
            for i in slide.num:
                num_str += str(i)+' '
            f.write(num_str + terminator)

