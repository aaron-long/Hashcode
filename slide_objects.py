class Photo:
    """
    Our basic photo object.
    """
    def __init__(self, orientation=None, num=0, tags=[]):
        self.orientation = orientation
        self.id = num
        self.tags = tags

    def __repr__(self):
        return "Photo ({0}): {1}".format(self.orientation, self.tags)


class Slide:
    """
    Our basic slide object.
    """
    def __init__(self, photo1=Photo(), photo2=None):
        if photo2 is None:
            self.orientation = photo1.orientation
            self.id = [photo1.id]
            self.tags = list(photo1.tags)
        else:
            self.orientation = photo1.orientation
            self.id = [photo1.id, photo2.id]
            self.tags = sorted(list(set(photo1.tags + photo2.tags)))

    def __repr__(self):
        return "Slide ({0}): {1}".format(self.id, self.tags)
