from dice import Die

class Layout(object):
    """
    A collection of starting dice, health, and armor for a particular
    class' major/minor attributes.

    Maybe in the future, starting equipment, and items will be covered too.

    This class instance's data is meant to be accumulated. Should a player choose
    a "Wizard" major and a "Fighter" minor, you should combine each of these
    major/minor attributes to create a complete player profile.
    """

    def __init__(self, dice=None, health=0, armor=0, agility=0):
        if dice is None:
            dice = []

        self.dice = dice
        self.health = health
        self.armor = armor
        self.agility = agility


class Rouge(object):
    major_dice = [Die('white')] * 5 + [Die('red')] + [Die('black')] * 3
    major = Layout(
        dice=major_dice,
        health=1,
        armor=1,
        agility=2
    )

    minor_dice = [Die('red')] + [Die('black')]
    minor = Layout(
        dice=dice,
        health=1,
        agility=1
    )


class Wizard(object):
    major_dice = [Die('white')] * 3 + [Die('blue')] * 3 + [Die('green')]
    major = Layout(
        dice=dice,
        health=1
    )

    minor_dice = [Die('blue')] + [Die('green')]
    minor = Layout(
        dice=dice
    )

class Cleric(object):
    major_dice = [Die('white')] * 4 + [Die('blue')] + [Die('green')] * 3
    major = Layout(
        dice=dice,
        health=1
    )

    minor_dice = [Die('blue')] + [Die('green')]
    minor = Layout(
        dice=dice
    )


class Fighter(object):
    major_dice = [Die('white')] * 6 + [Die('red')] * 3 + [Die('black')]
    major = Layout(
        dice=dice,
        health=1,
        armor=1,
        agility=1
    )

    minor_dice = [Die('red')] + [Die('black')]
    minor = Layout(
        dice=dice,
        armor=1,
        agility=1
    )


class Bard(object):
    major_dice = [Die('white')] * 4 + [Die('red')] + [Die('blue')] + [Die('black')] + [Die('green')]
    major = Layout(
        dice=dice,
        agility=1,
        health=1
    )

    minor_dice = [Die('red')] + [Die('blue')]
    minor = Layout(
        dice=dice,
        agility=1
    )
