# Wordl - written by: 
# Þorvarður Helgi Bjarnason | 0410992919 | thorvardur23@ru.is

from DLL import *
from Code import Code
from Frontend import PrintFunctions
from Scores import Scores

class Wordle:
    '''Run this file to play the game'''
    def __init__(self, word_length, num_of_guesses, Scores):
        self.word_length = word_length
        self.num_of_guesses = num_of_guesses
        self.Dll = DLL()
        self.Code = Code(word_length)
        self.Scores = Scores
        self.Print = PrintFunctions(word_length)
        self.message = "Waiting for the first guess"
        self.input_prompt()

    def get_code(self, guess):
        return self.Code.get_code(guess)

    def input_validation(self, guess):
        length = len(guess)
        if length < self.word_length:
            return "Input was too short"
        elif length > self.word_length:
            return "Input was too long"
        elif not guess.isalpha():
            return "Input must contain only alphabetical characters"
        return 0
    
    def __str__(self):
        ret_string = ""
        ret_string += self.Print.logo()
        ret_string += self.Print.print_header(f"Highscore: {self.Scores.highscore}   |   Current Score: {self.Scores.current_score}")
        ret_string += self.Print.empty_line()

        node = self.Dll.front.next
        for _ in range(self.Dll.size):
            ret_string += self.Print.row(node.word, node.code)
            node = node.next
        for n in range(num_of_guesses - self.Dll.size):
            ret_string += self.Print.empty_row(self.word_length)
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left(self.message)
        ret_string += self.Print.allign_left("[q] : quit")
        ret_string += self.Print.end_line()
        return ret_string

    def input_prompt(self):
        print(self)
        while True:
            guess = input(f"Input your {self.word_length} letter word guess: ").lower()
            
            if guess == "q":
                break
            error = self.input_validation(guess)
            if not error:
                code = self.get_code(guess)
                if code == "C"*self.word_length:
                    self.message = "Congratulations you win!"
                    self.Scores.add_score(((self.word_length * 3) // (self.Dll.size + 1)) * 100)
                    self.Dll.append(guess, code)
                    print(self)
                    break
                self.Dll.append(guess, code)
                self.message = "Waiting for the next guess"
            else:
                self.message = error
                self.input_prompt()
                break
            if self.Dll.size == self.num_of_guesses:
                self.message = f"You lose! The answer was '{self.Code.answer}'"
                self.Scores.reset_score()
                print(self)
                break
            print(self)



def word_length_valid(word_length):
    return word_length.isnumeric() and int(word_length) > 2 and int(word_length) < 10

def num_of_guesses_valid(word_length, num_of_guesses):
    word_length = int(word_length)
    return num_of_guesses.isnumeric() and int(num_of_guesses) >= 1 and int(num_of_guesses) <= (word_length + 5)

if __name__ == "__main__":
    print("press [q] to quit")
    Scores = Scores()
    inp = input(f"Press [Enter] to start a game: ")
    while inp != "q":

        word_length = input("What word length would you like? ")
        while not word_length_valid(word_length):
            print("")
            print("Word length must be between [3,9]")
            word_length = input("What word length would you like? ")
        word_length = int(word_length)

        num_of_guesses = input("How many guesses would you like to have? ")
        while not num_of_guesses_valid(word_length, num_of_guesses):
            print("")
            print(f"Number of guesses must be between [1,{word_length + 5}]")
            num_of_guesses = input("What word length would you like? ")
        num_of_guesses = int(num_of_guesses)

        wordle = Wordle(word_length, num_of_guesses, Scores)
        print("Would you like to play again?")
        inp = input("Press [Enter] to start, [q] to quit: ").lower()
    
