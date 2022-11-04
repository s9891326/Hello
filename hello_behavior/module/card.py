import abc


class Card(abc.ABC):
    name = None
    
    @abc.abstractmethod
    def execute(self, player, card: "Card"):
        return NotImplemented


class Guard(Card):
    name = "衛兵"
    
    def execute(self, player, card: "Card"):
        if card.name == player.hands[0]:
            player.out()


class Baron(Card):
    name = "男爵"
    
    def execute(self, player, card: "Card"):
        pass


class Priest(Card):
    name = "神父"
    
    def execute(self, player, card: "Card"):
        pass


ALL_CARDS = [Guard(), Baron(), Priest()]


def change_card_name_to_card(card_name: str):
    for card in ALL_CARDS:
        if card.name == card_name:
            return card
    return None
