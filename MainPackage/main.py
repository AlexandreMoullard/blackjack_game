from MainPackage.Classes import classes

class Game:

    in_game = True
    player = ''
    dealer = ''
    deck = []
    amount_in_game = 0

    def party(self):
        self.init_party()
        self.init_game()
        while self.in_game:
            self.playing()

    def init_party(self):
        self.dealer = classes.Dealer()
        self.player = classes.Player('john', 100)

    def init_game(self):
        self.deck = classes.Deck()
        self.deck.create_deck()
        self.deck.shuffle_deck()
        self.amount_in_game = self.player.bet()
        print('Amount accepted, your funds in game are: ${} \nNew balance: ${}\n'.format(self.amount_in_game, self.player.money))
        self.dealer.players_hand += self.dealer.distribute(self.deck, 2)
        self.player.players_hand += self.dealer.distribute(self.deck, 2)
        print('The dealer\'s visible card is: {} of {}'.format(self.dealer.players_hand[-1][1], self.dealer.players_hand[-1][0]))
        print('Your hand is:\n{}'.format(self.player.show_hand()))

    def playing(self):
        if not self.player.busted() and not self.dealer.busted():
            player_stands = self.player.play(self.deck, self.dealer)
            dealer_stands = self.dealer.play(self.deck, self.dealer)

            if player_stands and dealer_stands:
                if self.player.count_cards() >= self.dealer.count_cards():
                    print('You win, your hand:\n{}with a value of {}\n'.format(self.player.show_hand(), self.player.count_cards()))
                    print('is higher than or equal to the dealer\'s hand:\n{}\nwith a value of {}\n'.format(self.dealer.show_hand(), self.dealer.count_cards()))
                    self.player.money += 2*self.amount_in_game
                    print('You have now: ${}'.format(self.player.money))
                else:
                    print('You loose, your hand:\n{}with a value of {}\n'.format(self.player.show_hand(), self.player.count_cards()))
                    print('is lower than the dealer\'s hand:\n{}\nwith a value of {}\n'.format(self.dealer.show_hand(), self.dealer.count_cards()))
                    print('You have now: ${}'.format(self.player.money))
                self.end_game()
                self.continue_playing()
        
        else:
            if self.dealer.busted():
                print('You win! Your hand is:\n{}'.format(self.player.show_hand()))
                print('Dealer\'s hand is:\n{}'.format(self.dealer.show_hand()))
                self.player.money += 2*self.amount_in_game
                print('You have now: ${}'.format(self.player.money))
            
            elif self.player.busted():
                print('You loose! Your hand is:\n{}'.format(self.player.show_hand()))
                print('Dealer\'s hand is:\n{}'.format(self.dealer.show_hand()))
                print('You have now: ${}'.format(self.player.money))
            self.end_game()
            self.continue_playing()



  
    def continue_playing(self):
        if self.player.money > 0:
            wait_input = True
            while wait_input:
                try:
                    action = str(input('Do you want to continue playing (y/n): ')).lower()
                except:
                    print('Please enter \"y\" or \"n\"')
                else:
                    if action == 'y':
                        self.init_game()
                        wait_input = False
                    elif action == 'n':
                        self.in_game = False
                        wait_input = False
                    else :
                        print('Please enter \"y\" or \"n\"')

        else:
            self.in_game = False

    def end_game(self):
        del self.deck
        self.player.players_hand = []
        self.dealer.players_hand = []
        self.amount_in_game = 0