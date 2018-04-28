from random import shuffle

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
    	return sel.rank + 'of' + self.suit


class Deck:
    
    def __init__(self):
        self.deck = []
        self.suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def create_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append((suit, rank))

    def shuffle_deck(self):
        shuffle(self.deck)
        
    
    def draw(self, number_of_cards=1):
        cards_given = []
        for n in range(1, number_of_cards+1):
            cards_given.append(self.deck.pop())
        return cards_given
    

class Player():
    
    def __init__(self, name, money=0):
        self.players_hand  = []
        self.name  = name
        self.money = money
        
    def see_cards(self):
        print('Your cards are:{}'.format(self.show_hand()))
        
    def hit(self, deck_used, actual_dealer):
        card = actual_dealer.distribute(deck_used)
        self.players_hand.append(card[0])
        
    
    def stand(self):
        pass #stand is: not doing anything

    def bet(self):
        wait_input = True
        while wait_input:
            try:
                amount = abs(int(input("You have ${}. How much do you want to play: ".format(self.money))))
            except:
                print('Please insert a number')
            else:
                if self.money - amount < 0:
                    print('You dont have enough money:  {}'.format(self.money))
                else:
                    self.money = self.money - amount
                    self.amount_in_game = amount
                    wait_input = False
        return amount
    
    def count_cards(self):
        result = 0; ace_count = 0; maxi = 0
        for card in self.players_hand:
            result += values[card[1]]
            if card[1] == 'As':
                ace_count += 1
        
        while ace_count and result > 21:
            result -= 10
            ace_count -= 1

        #print(self.players_hand)
        #print(result)
        return result

    def busted(self):  
        return self.count_cards() > 21 
    
    def play(self, deck_used, actual_dealer):
        wait_input = True
        is_standing = False
        while wait_input:
            try:
                action = str(input('What do you play (hit / stand): ')).lower()
            except:
                print('Please enter \"hit\" or \"stand\"')
            else:
                if action == 'hit':
                    self.hit(deck_used, actual_dealer)
                    print('You recieved a new card: {} of {}'.format(self.players_hand[-1][1], self.players_hand[-1][0]))
                    print('Your hand is:\n{}'.format(self.show_hand()))
                    wait_input = False
                elif action == 'stand':
                    self.stand()
                    is_standing = True
                    wait_input = False
                else :
                    print('Please enter \"hit\" or \"stand\"')
        return is_standing

    def show_hand(self):
    	hand = ''
    	for card in self.players_hand:
    		hand += card[1] + ' of ' + card[0] + '\n'
    	return hand


class Dealer(Player):
    
    def __init__(self, name= 'bob', money=100000):
        self.amount_in_game = 0
        self.players_hand  = []
        self.name  = name
        self.money = money
    
    def distribute(self, deck_used, number_of_cards=1):
        cards = deck_used.draw(number_of_cards)
        return cards
              
    def play(self, deck_used, actual_dealer):              
        is_standing = False
        if self.count_cards() <= 17:
            self.hit(deck_used, actual_dealer)
            print('Dealer plays hit')
        else :
            self.stand()
            print('Dealer stands')
            is_standing = True
        return is_standing
      