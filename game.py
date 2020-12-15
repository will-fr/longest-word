# game.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string

class Game:
    def __init__(self):
        self.grid = []
        self.player_word=""
        for _ in range (9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def start_game(self):
        print ("WELCOME TO THE GAME ! ")
        print (f"The grid is : {self.grid}")
        while not self.is_valid(self.player_word):
            self.player_word = input("What is your word ? ")
            print (f"Your Word is : {self.player_word}")

    def is_valid(self, word):
        if not word:
            return False

        letters = self.grid.copy()
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True


def main():
    print ("starting...")
    game = Game()
    game.start_game()


if __name__ == "__main__":
    main()
