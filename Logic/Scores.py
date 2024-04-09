from Data.ScoreBST import ScoreBST

class Scores:
    def __init__(self, username = None):
        self.username = username

        self.filename = "Wordle\Data\scores.txt"
        file = open(self.filename, "r")
        score_list = file.read()
        score_list = score_list.split("\n")

        self.score_dict = ScoreBST()
        for line in score_list:
            username, score = line.split(",")
            self.score_dict.insert(username, int(score))

        self.highscore = self.get_highscore()
        self.current_score = 0
        self.score_dict[self.username] = self.current_score

    def __setitem__(self, username, score):
        self.score_dict[username] = score

    def __getitem__(self, username):
        return self.score_dict[username]

    def add_score(self, amount):
        '''Adds the score from the current game to total session score'''
        self.current_score += amount
        self.set_score()

    def set_score(self):
        self.score_dict[self.username] = self.current_score
    
    def reset_score(self):
        self.current_score = 0
    
    def is_highscore(self, score):
        return score > int(self.highscore["score"])

    def get_highscore(self):
        node = self.score_dict.get_highscore()
        return {"username" : node.username, "score" : node.score}

    def get_topten(self):
        ret_list = str(self.score_dict).split("\n")
        print(ret_list)
        return ret_list[0:10]
    
    def update_database(self):
        file = open(self.filename, "w")
        file.write(str(self.score_dict))
        file.close()
        
        file = open(self.filename, "r")
        score_list = file.read()
        score_list = score_list.split("\n")
        self.score_dict = ScoreBST()
        for line in score_list:
            username, score = line.split(",")
            self.score_dict.insert(username, score)

if __name__ == "__main__":
    score = Scores()
    score["TOR"] = 500
    score["ADJ"] = 450
    score["SAE"] = 450
    score["TOR"] = 300
    score["ADJ"] = 600
    print(score)


    