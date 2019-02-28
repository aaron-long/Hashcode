class Photo:
    """
    Our basic photo object
    """
    def __init__(self, orientation=None, num=0, tags=[], ):
        self.orientation = orientation
        self.num = num
        self.tags = tags

    def __repr__(self):
        return "Photo ({}): {}".format(self.orientation, self.tags)


class Slide:
    """
    A collection of ordered photos

    """
    def __init__(self, photo1=Photo(), photo2=None):
        if photo2 == None:
            self.num = [photo1.num]
            self.tags = list(photo1.tags)
        else:
            self.num = [photo1.num, photo2.num]
            self.tags = list(set(photo1.tags + photo2.tags))


def sort_photos(photos):
    """
    Sort photos so verticle photos are paired

    """
    slides = []
    last_vert = None
    for photo in photos:
        if photo.orientation == 'H':
            slides.append(Slide(photo))
        elif photo.orientation == 'V':
            if last_vert is None:
                last_vert = photo
            else:
                slides.append(Slide(last_vert, photo))
                last_vert = None
    return slides
