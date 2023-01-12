
class Player :
    def __init__(self, name: str, cards_num: int = 26) :
        if cards_num > 26 or cards_num < 10 :
            cards_num = 26
        self.name = name
        self.cards_num = cards_num
        self.player_hand = []

    def set_hand(self, deck1:) :
        for i in range(self.cards_num) :
            self.player_hand.append(deck1.del_one())