from typing import List


class Player:
    def __init__(self, name: str, hands: List["Card"]):
        self.name = name
        self.hands = hands
        self.am_i_out = False
        self.protected = False
    
    def play(self, opponent: "Player", play_card: "Card", card: "Card"):
        if not opponent.protected:
            play_card.execute(opponent, card)
        
        self.hands.remove(play_card.name)
    
    def out(self):
        self.am_i_out = True
