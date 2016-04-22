from player import Player
from layout import Fighter
from layout import Rouge
import unittest

# run python -m src.test.test_player

fighter_player = Player(Fighter, Rouge)

class TestFighter(unittest.TestCase):

    def test_dice(self):
        self.assertEquals(fighter_player.major_class.major_dice, Fighter.major_dice)

if __name__ == '__main__':
    unittest.main()
