class Photo:
    """
    Our basic photo object
    """
    def __init__(self, orientation=None, num=None, tags=None, ):
        self.orientation = orientation
        self.num = num
        self.tags = tags

    def __repr__(self):
        return "Photo ({}): {}".format(self.orientation, self.tags)


class Slide:
    """
    A collection of ordered photos

    """
    def __init__(self, photo1=None, photo2=None):
        self.num = [photo1.num, photo2.num]
        self.tags = list(set(photo1.tags + photo2.tags))


def sort_photos(photos):
    pass
