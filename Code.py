import random

class Code:
    def __init__(self, word_length):
        self.answer = self.get_answer(word_length)
    
    def get_answer(self, word_length):
        """
        Read all five letter words in the Word Bank textfile

        Returns, return: One random five letter word.
        """
        filename = f"Wordle\wordbank_{word_length}.txt"
        file = open(filename, "r")
        words = file.read()

        word_list = words.split("\n")
        random_word = random.choice(word_list)
        return random_word.lower()

    def get_code(self, guess): #O(n)
        '''
        Input, {word_length} letter word
        Compares input to random word from wordbank.txt
        "C" : correct letter in correct place
        "c" : correct letter in wrong place
        "-" : incorrect letter

        Returns, return: {word_length} letter code comparing input to answer (format ex: "-C--c")
        '''
        code = ""
        answer_count = {}
        guess_count = {}
        
        # Count occurrences of each letter in answer and guess
        for a, g in zip(self.answer, guess):
            answer_count[a] = answer_count.get(a, 0) + 1
            guess_count[g] = guess_count.get(g, 0) + 1

        for n in range(len(guess)):
            if guess[n] not in self.answer:
                code += "-"
            elif guess[n] == self.answer[n]:
                code += "C"
            else: # guess[n] in self.answer
                  # compares the counts of letter in answer to count of letter in guess
                  # prevents guess = "ddddd", answer = "wordl", giving code = "cccCc"
                if guess_count[guess[n]] > answer_count[guess[n]]:
                    guess_count[guess[n]] -= 1
                    code += "-"
                else:
                    code += "c"
        return code