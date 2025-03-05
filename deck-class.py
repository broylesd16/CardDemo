import random
from playing_card import PlayingCard

class Deck:
    """A class representing a standard 52-card deck of playing cards"""
    
    def __init__(self):
        """Initialize a full deck of 52 cards"""
        self.cards = self.generate_deck()
    
    def generate_deck(self):
        """Generate a full deck of 52 unique cards"""
        return [
            PlayingCard(rank, suit) 
            for suit in PlayingCard.SUITS 
            for rank in PlayingCard.RANKS
        ]
    
    def shuffle(self):
        """Shuffle the deck of cards randomly"""
        random.shuffle(self.cards)
    
    def draw(self):
        """
        Draw a card from the deck.
        
        Returns:
            PlayingCard: A card drawn from the top of the deck
        
        Raises:
            IndexError: If the deck is empty
        """
        if not self.cards:
            raise IndexError("Cannot draw from an empty deck")
        return self.cards.pop()
    
    def __len__(self):
        """Return the number of cards remaining in the deck"""
        return len(self.cards)
