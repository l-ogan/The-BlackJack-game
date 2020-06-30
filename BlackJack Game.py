#Here values act as global variable so values[rank] will give value of rank ie jack ace two three etc
import random
suits=("Hearts","Diamounds","Clubs","Spades")
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
value={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,
       "Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank            #This whole calss represents a single card ie Two of Hearts or jack of spades
        self.value=value[rank]
    def __str__(self):
        return self.rank+" Of "+self.suit


class Deck:
    def __init__(self):
        self.all_cards=[] #after going through 2 for loops all_cards willl have all 52 cards with suit and rank
        for suit in suits:
            for rank in ranks:
                card=Card(suit,rank) #it will take suit and rank and card instant willl be created and added to all_cards
                #Create a card object
                self.all_cards.append(card) #card at each instant will be add to list of all_cards
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
        
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"


#Game Setup
player_one=Player("One")
player_two=Player("Two")
new_deck=Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


#Game on
round=0
game_on=True
while game_on:
    round+=1
    print(f"Round {round}")
    # Win check
    if len(player_one.all_cards)==0:
        print("Player 1 has no cards left!. Player 2 has won the game")
        game_on=False
        break
    if len(player_two.all_cards)==0:
        print("Player 2 has no cards left!. Player 1 has won the game")
        game_on=False
        break
    # payer 1 given a card    
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())
    # player 2 has given a card
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())
    
    # Check whether they are at war or not ie rank of both 1 and 2's card are same
    # when at war each player will put 5 card on table and next winner takes it all
    # if any player dont have enough 5 cards to palce he looses
    
    at_war=True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war=False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war=False
            
        else:
            print("WAR!")
            if len(player_one.all_cards)<5: #drawing 5 cards at war the game will be short if u choose 3 the game will be much long
                print("Player 1 is unable to declare war")
                print("Player 2 has won the game")
                game_on=False
                break
            elif len(player_two.all_cards)<5:
                print("Player 1 is unable to declare war")
                print("Player 2 has won the game")
                game_on=False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    
            
