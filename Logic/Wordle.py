# Wordl - written by: 
# Þorvarður Helgi Bjarnason | 0410992919 | thorvardur23@ru.is

from Data.DLL import *
from Logic.Code import Code
from Ui.PrintFunctions import PrintFunctions
#from Logic.Scores import Scores

class Wordle:
    '''Run this file to play the game'''
    def __init__(self, word_length, num_of_guesses, Scores):
        self.word_length = word_length
        self.num_of_guesses = num_of_guesses
        self.Dll = DLL()
        self.Code = Code(word_length)
        self.Scores = Scores
        self.Print = PrintFunctions()
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
        if self.Scores.current_score == -1:
            ret_string += self.Print.print_header("Wordle")
        else:
            ret_string += self.Print.print_header(f"Highscore: {self.Scores.highscore["username"]}: {self.Scores.highscore["score"]}   |   Current Score: {self.Scores.current_score}")
        ret_string += self.Print.empty_line()

        node = self.Dll.front.next
        for _ in range(self.Dll.size):
            ret_string += self.Print.row(node.word, node.code)
            node = node.next

        for n in range(self.num_of_guesses - self.Dll.size):
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

                    if self.Scores.current_score != -1:
                        self.Scores.add_score(((self.word_length * 3) // (self.Dll.size + 1)) * 100)
                        self.Scores.update_database()

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
                if self.Scores.current_score != -1:
                    self.Scores.reset_score()
                print(self)
                break
            
            print(self)