from Logic.Scores import Scores
from Ui.PrintFunctions import PrintFunctions
from Logic.Wordle import Wordle

class MainMenu:
    def __init__(self):
        self.Print = PrintFunctions()
        self.main_menu()

    def ask_version(self):
        ret_string = ""
        ret_string += self.Print.logo()
        ret_string += self.Print.print_header("Þorvarður Helgi Bjarnason | 0410992919 | thorvardur23@ru.is")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("Select Version")
        ret_string += self.Print.allign_left("[1] : User loggin")
        ret_string += self.Print.allign_left("      This version allows you to see previous users score history")
        ret_string += self.Print.allign_left("      As well as save your score into the database")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("[2] : Basic Wordl")
        ret_string += self.Print.allign_left("      You just want to play Wordle")
        ret_string += self.Print.allign_left("      no strings (or score keeping) attached")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("[3] : Add Words")
        ret_string += self.Print.allign_left("      Add any words to our amazing wordbanks")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("[Any other key] : Exit")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.end_line()
        print(ret_string)
        return input("Waiting for input: ")

    def ask_username_helper(self, message):
        ret_string = ""
        ret_string += self.Print.logo()
        ret_string += self.Print.print_header("ULTRA HARDCORE GAMER MODE ACTIVATED")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("Input your 3 letter GAMER USERNAME")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left(message)
        ret_string += self.Print.empty_line()
        ret_string += self.Print.end_line()
        print(ret_string)
        return input("Waiting for input: ")
    
    def username_valid(self, username):
        return len(username) == 3

    def ask_username(self):
        username = self.ask_username_helper("")
        while not self.username_valid(username):
            message = "Username must be 3 characters (ex: AAA)"
            username = self.ask_username_helper(message)
        return username

    def word_length_valid(self, word_length):
        return word_length.isnumeric() and int(word_length) > 2 and int(word_length) < 10

    def ask_wordlength_helper(self, message):
        ret_string = ""
        ret_string += self.Print.logo()
        ret_string += self.Print.print_header("Starting Game")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("Word Length")
        ret_string += self.Print.allign_left("The database allows for words of length 3 to 9")
        ret_string += self.Print.allign_left("Longer words provide higher scores")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("Number of Guesses")
        ret_string += self.Print.allign_left("The Game will permit guesses from 1 to word_length + 5")
        ret_string += self.Print.allign_left("Fewer guesses provide higher scores")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left(message)
        ret_string += self.Print.empty_line()
        ret_string += self.Print.end_line()
        print(ret_string)
        return input("Waiting for input: ")

    def ask_wordlength(self):
        word_length = self.ask_wordlength_helper("Input Word Length: ")
        while not self.word_length_valid(word_length):
            message = "Word length must be a valid integer between 3 and 9"
            word_length = self.ask_wordlength_helper(message)
        return int(word_length)

    def num_of_guesses_valid(self, word_length, num_of_guesses):
        word_length = int(word_length)
        return num_of_guesses.isnumeric() and int(num_of_guesses) >= 1 and int(num_of_guesses) <= (word_length + 5)

    def ask_num_of_guesses_helper(self, message, word_length):
        ret_string = ""
        ret_string += self.Print.logo()
        ret_string += self.Print.print_header("Starting Game")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("Word Length:")
        ret_string += self.Print.allign_left(f"{word_length}")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("Number of Guesses")
        ret_string += self.Print.allign_left("The Game will permit guesses from 1 to word_length + 5")
        ret_string += self.Print.allign_left("Fewer guesses provide higher scores")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left(message)
        ret_string += self.Print.empty_line()
        ret_string += self.Print.end_line()
        print(ret_string)
        return input("Waiting for input: ")

    def ask_num_of_guesses(self, word_length):
        num_of_guesses = self.ask_num_of_guesses_helper("Input Number of Guesses: ", word_length)
        while not self.num_of_guesses_valid(word_length, num_of_guesses):
            message = f"Number of guesses must be between [1,{word_length + 5}]"
            num_of_guesses = self.ask_num_of_guesses_helper(message, word_length)
        return int(num_of_guesses)

    def show_score_history(self, username = None):
        print_format = "%-5s%-10s%-15s"
        score_list = self.Scores.get_topten()
        n = 0

        ret_string = ""
        ret_string += self.Print.logo()
        ret_string += self.Print.print_header("Score history")
        ret_string += self.Print.empty_line()

        ret_string += self.Print.allign_left(print_format % ("Nr", "Username", "Score"))
        for user in score_list:
            username, score = user.split(",")
            ret_string += self.Print.allign_left(print_format % (n + 1, username, score))
            n += 1

        for m in range(n, 10):
            ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("Press [Enter] to start a game, [q] to quit")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.end_line()
        print(ret_string)
        inp = input("Waiting for input: ")
        if inp != "q":
            self.run_game(username)

    def add_words_ui_helper(self, error_message):
        ret_string = ""
        ret_string += self.Print.logo()
        ret_string += self.Print.print_header("Adding Words")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("You have decided that my massive collection of words")
        ret_string += self.Print.allign_left("is not enough... so be it")
        ret_string += self.Print.allign_left("")
        ret_string += self.Print.allign_left("The word can be any word of length 3-9")
        ret_string += self.Print.allign_left("Go ahead, do your thing, I'm waiting for your correct input")

        ret_string += self.Print.empty_line()
        ret_string += self.Print.allign_left("[q] : quit")
        ret_string += self.Print.empty_line()
        ret_string += self.Print.end_line()
        print(ret_string)
        return input("Waiting for input: ")
    
    def add_word_validation(self, word):
        return word == "q" or (2 < len(word) < 10 and word.isalpha())

    def add_words_ui(self):
        word = self.add_words_ui_helper("")
        while not self.add_word_validation(word):
            word = self.add_words_ui_helper("Word must contain only letters and be between 3 and 9 letters long")
        if word != "q":
            self.add_word(word)
        self.main_menu()

    def add_word(self, word):
        filename = f"Wordle\Data\wordbank_{len(word)}.txt"
        file = open(filename, "a")
        file.write("\n" + word)
        print(f"{word} has been added to wordbank_{len(word)}.txt")

    def main_menu(self):
        version = self.ask_version()
        
        if version == "1": # User loggin
            username = self.ask_username().upper()
            self.Scores = Scores(username)
            self.show_score_history(username)

        elif version == "2": # Basic Wordl
            self.Scores = Scores()
            self.run_game()

        elif version == "3": # Add word to wordbanks
            self.add_words_ui()

    def run_game(self, username = None):
        if username is None:
            self.Scores.current_score = -1
            
        inp = ""
        while inp != "q":

            word_length = self.ask_wordlength()
            num_of_guesses = self.ask_num_of_guesses(word_length)

            wordle = Wordle(word_length, num_of_guesses, self.Scores)
            print("Would you like to play again?")
            if username is None:
                inp = input("Press [Enter] to start, [q] to quit: ").lower()
            else:
                inp = input("Press [Enter] to start, [q] to quit, [b] to go back to the MainMenu: ").lower()

            if inp == "b" and username is not None:
                self.show_score_history(username)
                break #I know this could be a stacking issue, just ... idk

if __name__ == "__main__":
    game = MainMenu()