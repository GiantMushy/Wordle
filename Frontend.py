class PrintFunctions:
    def __init__(self, word_length):
        #9 -> 0, 8 -> 0, 7 -> 1, 6 -> 1, 5 -> 2, 4 -> 2, 3 -> 3
        self.size_of_left_empty_space = (9 - (word_length + (word_length + 1)%2))//2
        self.size_of_right_empty_space = (self.size_of_left_empty_space + ((word_length + 1)%2))

        

    def empty_line(self):
        '''Returns the printable string of an empty line'''
        return "║                                                                          ║" + "\n"
    
    def word_to_grid(self, word): #O(idk_lol)
        word_length = len(word)
        ret_string = "║ " + ("        " * self.size_of_left_empty_space)
        for n in range(word_length):
            ret_string += f"|  {word[n]}  | "
        ret_string += "        " * self.size_of_right_empty_space + " ║"
        return ret_string

    def row(self, word, code):
        word = word.upper()
        ret_string = ""
        ret_string += self.word_to_grid(word.upper()) + "\n"
        ret_string += self.word_to_grid(code) + "\n"
        ret_string += "║ " + "        " * self.size_of_left_empty_space
        ret_string += "════════" * len(word)
        ret_string += "        " * self.size_of_right_empty_space + " ║" + "\n"
        return ret_string

    def empty_row(self, word_length):
        return self.row(" " * word_length, " " * word_length)

    def allign_left(self, text):
        '''Returns the printable string of an empty line'''
        return f"║      {text + (' ' * (66 - len(text)))}  ║" + "\n"

    def end_line(self):
        '''Returns the printable string of the end line ui'''
        return "╚══════════════════════════════════════════════════════════════════════════╝" + "\n"

    def print_header(self, text):
        '''Prints the header of the interface'''
        ret_string = ""
        ret_string += "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█" + "\n"
        str_length = len(text)
        spaces = (74 - str_length)
        odd_even = spaces % 2
        left_spaces = (spaces - odd_even) * 0.5
        left_spaces = int(left_spaces)
        right_spaces = (spaces + odd_even) * 0.5
        right_spaces = int(right_spaces)
        ret_string += "█" + (" " * left_spaces) + text + (" " * right_spaces) + "█" + "\n"
        ret_string += "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█" + "\n"
        return ret_string
    
    def logo(self):
        ret_string = "\n"
        ret_string += "▀████▀     █     ▀███▀ ▄▄█▀▀██▄ ▀███▀▀▀██▄ ▀███▀▀▀██▄ ▀████▀   ▀███▀▀▀███" + "\n"
        ret_string += "  ▀██     ▄██     ▄█ ▄██▀    ▀██▄ ██   ▀██▄  ██    ▀██▄ ██       ██    ▀█ " + "\n"
        ret_string += "   ██▄   ▄███▄   ▄█  ██▀      ▀██ ██   ▄██   ██     ▀██ ██       ██   █   " + "\n"
        ret_string += "    ██▄  █▀ ██▄  █▀  ██        ██ ███████    ██      ██ ██       ██████   " + "\n"
        ret_string += "    ▀██ █▀  ▀██ █▀   ██▄      ▄██ ██  ██▄    ██     ▄██ ██     ▄ ██   █ ▄" + "\n"
        ret_string += "     ▄██▄    ▄██▄    ▀██▄    ▄██▀ ██   ▀██▄  ██    ▄██▀ ██    ▄█ ██    ▄█" + "\n"
        ret_string += "      ██      ██       ▀▀████▀▀ ▄████▄ ▄███▄████████▀ ██████████ ████████" + "\n"
        return ret_string

if __name__ == "__main__":
    word_length= 3
    Print = PrintFunctions(word_length)
    string = ""
    string += Print.logo()
    string += Print.print_header("Wordl")
    string += Print.empty_line()
    string += Print.row("h"*word_length, "-"*word_length)
    string += Print.empty_row(word_length)
    string += Print.end_line()
    print(string)