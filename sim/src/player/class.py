import dice

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

    @staticmethod
    @property
    def major():
        dice = ['white'] * 5 + ['red'] + ['black'] * 3

        return Layout(
            dice=dice,
            health=1,
            armor=1,
            agility=2
        )

    @staticmethod
    @property
    def minor():
        dice = ['red', 'black']

        return Layout(
            dice=dice,
            health=1,
            agility=1
        )


class Wizard(object):

    @staticmethod
    @property
    def major():
        dice = ['white'] * 3 + ['blue'] * 3 + ['green']

        return Layout(
            dice=dice,
            health=1
        )

    @staticmethod
    @property
    def minor():
        dice = ['blue'] + ['green']

        return Layout(
            dice=dice
        )

class Cleric(object):

    @staticmethod
    @property
    def major():
        dice = ['white'] * 4 + ['blue'] + ['green'] * 3

        return Layout(
            dice=dice,
            health=1
        )

    @staticmethod
    @property
    def minor():
        dice = ['blue'] + ['green']
        return Layout(
            dice=dice
        )


class Fighter(object):

    @staticmethod
    @property
    def major():
        dice = ['white'] * 6 + ['red'] * 3 + ['black']

        return Layout(
            dice=dice,
            health=1,
            armor=1,
            agility=1
        )

    @staticmethod
    @property
    def minor():
        dice = ['red'] + ['black']

        return Layout(
            dice=dice,
            armor=1,
            agility=1
        )


class Bard(object):

    @staticmethod
    @property
    def major():
        dice = ['white'] * 4 + ['red', 'blue', 'black', 'green']

        return Layout(
            dice=dice,
            agility=1,
            health=1
        )

    @staticmethod
    @property
    def minor():
        dice = ['red'] + ['blue']

        return Layout(
            dice=dice,
            agility=1
        )
