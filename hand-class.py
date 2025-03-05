class Hand:
    """A class representing a hand of playing cards"""
    
    def __init__(self):
        """Initialize an empty hand"""
        self.cards = []
    
    def add_card(self, card):
        """
        Add a card to the hand
        
        Args:
            card (PlayingCard): The card to add to the hand
        """
        self.cards.append(card)
    
    def display(self):
        """
        Generate a string representation of the hand
        
        Returns:
            str: A string listing all cards in the hand
        """
        return ", ".join(str(card) for card in self.cards) if self.cards else "Empty hand"
    
    def __len__(self):
        """
        Return the number of cards in the hand
        
        Returns:
            int: Number of cards in the hand
        """
        return len(self.cards)
