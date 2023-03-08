import unittest

from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.ace = Card("Spades", 1)
        self.ten_of_hearts = Card("Hearts", 10)
        self.eight_of_hearts = Card("Hearts", 8)
        self.match = CardGame()


    def test_can_spot_ace(self):
        self.assertEqual(True, self.match.check_for_ace(self.ace))

    def test_will_return_highest_card(self):
        self.assertEqual(self.ten_of_hearts, self.match.highest_card(self.ten_of_hearts, self.eight_of_hearts))

    def test_can_total_cards(self):

        list_of_cards = [self.ten_of_hearts, self.eight_of_hearts]

        self.assertEqual("You have a total of 18", self.match.cards_total(list_of_cards))
