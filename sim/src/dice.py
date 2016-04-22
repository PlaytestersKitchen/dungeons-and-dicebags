import random

class Die(object):
    """
    A dice object. It has a color, and numbers.
    In the future, it may end up supporting symbols instead, if numbers
    are too boring to keep player's interest.
    """

    def __init__(self, color, sides=range(1, 7)):
        self.color = color
        self.sides = sides

    def roll(self):
        return (self.color, random.choice(self.sides))

class Dicebag(object):
    """
    The player's collection of dice objects.
    """

    def __init__(self, dice=None):
        if dice is None:
            dice = []

        self.dice = dice

    def __len__(self):
        return len(self.dice)

    def draw(self, limit):
        return random.sample(self.dice, limit)

    @staticmethod
    def roll(dice):
        """ `draw` your own dice and roll them here. """
        return [d.roll() for d in dice]

    @staticmethod
    def colors(dice):
        """ `draw` your own dice and get the colors you pulled here. """
        return [d.color for d in dice]
