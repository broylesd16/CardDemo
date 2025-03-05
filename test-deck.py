import unittest
import random
from deck import Deck
from playing_card import PlayingCard

class TestDeck(unittest.TestCase):
    def setUp(self):
        """Create a fresh deck before each test"""
        self.deck = Deck()
    
    def test_deck_initialization(self):
        """Test that a new deck has 52 cards"""
        self.assertEqual(len(self.deck.cards), 52)
    
    def test_unique_cards(self):
        """Ensure all cards in the deck are unique"""
        unique_cards = set(self.deck.cards)
        self.assertEqual(len(unique_cards), 52)
    
    def test_shuffle(self):
        """
        Test that shuffle changes the order of cards.
        Note: While not 100% guaranteed, the probability of 
        the deck remaining in the exact same order after shuffling 
        is extremely low.
        """
        # Set a fixed seed for reproducibility
        random.seed(42)
        original_order = self.deck.cards.copy()
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.cards)
    
    def test_draw(self):
        """Test drawing a card from the deck"""
        initial_length = len(self.deck)
        card = self.deck.draw()
        
        # Check that the card is a PlayingCard
        self.assertIsInstance(card, PlayingCard)
        
        # Check that the deck size decreased
        self.assertEqual(len(self.deck), initial_length - 1)
    
    def test_draw_empty_deck(self):
        """Test drawing from an empty deck raises an IndexError"""
        # Draw all cards
        while len(self.deck) > 0:
            self.deck.draw()
        
        # Try to draw from an empty deck
        with self.assertRaises(IndexError):
            self.deck.draw()

if __name__ == "__main__":
    unittest.main()
