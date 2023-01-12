from random import randint
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
        if len(deck1.cards) < self.cards_num :
            raise ValueError("Deck is out of cards")
        for c in range(self.cards_num):
            self.player_hand.append(deck1.del_one())
    def get_card(self):
        if len(self.player_hand) == 0 :
            raise IndexError("Player is out of cards")
        return self.player_hand.pop()
    def add_card(self, card) :
        if type(card) != Card:
            raise TypeError("Invalid card object")
        self.player_hand.append(card)
class CardGame:
    def __init__(self, player1_name:str, player2_name:str, cards_num:int = 26):
        if cards_num > 26 or cards_num < 10 :
            cards_num = 26
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.cards_num = cards_num
        self.deck = DeckOfCards()
        self.player1 = Player(self.player1_name, self.cards_num)
        self.player2 = Player(self.player2_name, self.cards_num)
        self.new_game()
    def new_game(self):
        if len(self.player1.player_hand) >0 or len(self.player2.player_hand)>0:
            print("Error")
            return
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)
    def winner_game(self):
        if len(self.player1.player_hand) == len(self.player2.player_hand):
            return None
        print("no winner it is a tie")
        if len(self.player1.player_hand) > len(self.player2.player_hand) :
            print("player 1 winns")
        elif len(self.player1.player_hand) < len(self.player2.player_hand) :
            print("player 2 winns")
        else:
            return None
        print("no winner it is a tie")
if __name__ == '__main__' :







