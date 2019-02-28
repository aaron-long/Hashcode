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


def create_slideshow(photos):
    """
    Output photos list into a slideshow

    """
    for photo in photos:

