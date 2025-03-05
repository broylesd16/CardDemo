import unittest
from hand import Hand
from playing_card import PlayingCard

class TestHand(unittest.TestCase):
    def setUp(self):
        """Create a fresh hand before each test"""
        self.hand = Hand()
    
    def test_initial_hand_is_empty(self):
        """Test that a new hand is empty"""
        self.assertEqual(len(self.hand), 0)
        self.assertEqual(self.hand.display(), "Empty hand")
    
    def test_add_card(self):
        """Test adding a card to the hand"""
        card = PlayingCard("A", "Hearts")
        self.hand.add_card(card)
        
        self.assertEqual(len(self.hand), 1)
        self.assertEqual(self.hand.display(), "A of Hearts")
    
    def test_add_multiple_cards(self):
        """Test adding multiple cards to the hand"""
        cards = [
            PlayingCard("A", "Hearts"),
            PlayingCard("K", "Spades"),
            PlayingCard("10", "Diamonds")
        ]
        
        for card in cards:
            self.hand.add_card(card)
        
        self.assertEqual(len(self.hand), 3)
        self.assertEqual(
            self.hand.display(), 
            "A of Hearts, K of Spades, 10 of Diamonds"
        )

if __name__ == "__main__":
    unittest.main()
