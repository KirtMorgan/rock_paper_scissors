import random
class rock_paper_scissors():
    def __init__(self):
        self.player_input = 'nothing'
        self.computer_input = 'nothing'

    def get_user_input(self):
        user_input = input('Enter Rock, Paper or Scissors')
        self.player_input = user_input

    def generate_computer_input(self):
        options = ['rock', 'paper', 'scissors']
        rand_int = random.randint(0, 2)
        self.computer_input = options[rand_int]
        print('The computer chose', self.computer_input)

    def game_result(self):
        if self.player_input == self.computer_input:
            return 'You Tied'
        elif self.player_input == 'rock' and self.computer_input == 'paper':
            return 'You Lose'
        elif self.player_input == 'rock' and self.computer_input == 'scissors':
            return 'You Win'
        elif self.player_input == 'paper' and self.computer_input == 'rock':
            return 'You Win'
        elif self.player_input == 'paper' and self.computer_input == 'scissors':
            return 'You Lose'
        elif self.player_input == 'scissors' and self.computer_input == 'paper':
            return 'You Win'
        elif self.player_input == 'scissors' and self.computer_input == 'rock':
            return 'You Win'
        else:
            return 'Please type rock, paper or scissors'

    def run_game(self):
        while True:
            self.get_user_input()
            self.generate_computer_input()
            print(self.game_result())

            player_option_input = input('Play again? y/n')
            if player_option_input == 'n':
                break

game = rock_paper_scissors()
game.run_game()


