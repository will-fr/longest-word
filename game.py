# game.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string
import requests



class Game:
    def __init__(self):
        self.grid = []
        self.player_word=""
        self.playing=True


        for _ in range (9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def start_game(self):
        print ("WELCOME TO THE GAME ! ")
        print (f"The grid is : {self.grid}")
        while self.playing:
            self.player_word = input("What is your word ? ")
            print (f"Your Word is : {self.player_word}")

            if not self.is_valid(self.player_word):
                print ("Word not ok !")
                continue

            print ("Your word is valid ! ")
            playing = False


    def is_valid(self, word):
        if not word:
            print ("<err>Entrez un mot !")
            return False

        letters = self.grid.copy()
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                print ("<err>lettres incorrectes")
                return False


        return self.is_in_dictionary(word)

    def is_in_dictionary(self, word):
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = r.json()
        return json_response['found']

def main():
    print ("starting...")
    game = Game()
    game.start_game()


if __name__ == "__main__":
    main()
