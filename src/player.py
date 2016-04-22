class Player(object):
    """
    The layout has a class, which is made up of a major trait and a minor trait.
    They also collect items, weapons, and gear.
    """

    def __init__(self, major_class, minor_class):
        self.major_class = major_class
        self.minor_class = minor_class
