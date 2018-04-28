from random import shuffle

class Deck:
    
    cards = [10]*2*4 + list(range(1,10))*4 + ['As']*4

    def shuffle_deck(self):
        shuffle(self.cards)
        return self.cards
    
    def draw(self, number_of_cards=1):
        cards_given = []
        for n in range(1, number_of_cards+1):
            cards_given.append(self.cards.pop())
        return cards_given
    
    
class Dealer(Deck):
    
    dealers_hand  = []
    
    def distribute(self, number_of_cards=1):
        cards = self.draw(number_of_cards)
        return cards

    def stand(self):
        return True
        
    def hit(self):
        card = self.distribute()
        print(card)
        new_card = self.dealers_hand.append(card[0])
        return False
    
    def count_cards(self):
        result = 0
        for card in self.dealers_hand:
            if card != 'As':
                result += card
            else:
                if result + 11 <= 21:
                    result += 11
                else:
                    result += 1
        print(self.dealers_hand)
        print(result)
        return result
    
    def busted(self):  
        return self.count_cards() > 21 
    
    def play(self):              
        if self.count_cards() <= 17:
            pl = self.hit()
        else :
            pl = self.stand()
        return pl


class Player(Dealer):
    
    amount_in_game = 0
    players_hand  = []
    
    def __init__(self, name, money=0):
        self.name  = name
        self.money = money
        
    def see_cards(self):
        print('Your cards are:{}'.format(self.players_hand))
        
    def hit(self):
        card = self.draw()
        self.players_hand.append(card[0])
        print('You recieved a new card: {}'.format(card[0]))
        return False
    
    def bet(self):
        wait_input = True
        while wait_input:
            try:
                amount = abs(int(input("How much do you want to play: ")))
            except:
                print('Please insert a number')
            else:
                if self.money - amount <= 0:
                    print('You dont have enough money:  {}'.format(self.money))
                else:
                    self.money = self.money - amount
                    self.amount_in_game = self.amount_in_game + amount
                    print('Amount accepted, your funds in game are: ${} \nNew balance: ${}'.format(self.amount_in_game, self.money))
                    wait_input = False
    
    def count_cards(self):
        result = 0; ace_count = 0; maxi = 0
        for card in self.players_hand:
            if card != 'As':
                result += card
            else:
                ace_count += 1
        for i in range(1, ace_count+1):
            if result + ace_count -i + i*11 <= 21:
                maxi = result + ace_count -i + i*11
            else:
                result = result + ace_count
        if maxi > 0:
            result = maxi

        print(self.players_hand)
        print(result)
        return result
    
    def play(self):
        wait_input = True
        while wait_input:
            try:
                action = str(input('What do you play (hit / stand): ')).lower()
            except:
                print('Please enter \"hit\" or \"stand\"')
            else:
                if action == 'hit':
                    pl = self.hit()
                    wait_input = False
                elif action == 'stand':
                    pl = self.stand()
                    wait_input = False
                else :
                    print('Please enter \"hit\" or \"stand\"')
        return pl
        
