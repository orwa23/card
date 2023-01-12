
class Card:
    def __init__(self,suit:str,value:int):
        self.value=value
        self.suit=suit
        self.suits={"Diamonds":1,"Spades":2,"Hearts":3,"Clubs":4}
    def __gt__(self, other) :
        if self==other:
            print("error")
            return False
        if self.value == other.value :
            if self.suits[self.suit] > self.suits[other.suit] :
                return True
            else: return False
        elif self.value>other.value:
            if other.value==1:
                return False
            return True
        elif self.value<other.value:
            if self.value==1:
                return True
            return False
    def __eq__(self, other) :
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False

class DeckOfCards:
    def __init__(self):
        self.cards=[]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        for suit in suits :
            for rank in ranks :
                self.cards.append(Card(suit,rank))
                if len(self.cards) == 52 :
                    break
    def cards_shuffle(self) :
        from random import shuffle
        shuffle(self.cards)
    def del_one(self):
        if len(self.cards)==0:
            return 0
        return self.cards.pop()
class Player:
    def __init__(self, name:str, cards_num:int = 26):
        if cards_num > 26 or cards_num < 10 :
            cards_num = 26
        self.name=name
        self.cards_num=cards_num
        self.player_hand=[]

    def set_hand(self, deck1:DeckOfCards):
        for i in range(self.cards_num):
            self.player_hand.append(deck1.del_one())
    def get_card(self):
        from random import randint
        if len(self.cards_num)==0:
            return 0
        return self.player_hand.pop()

