class Scores:
    def __init__(self):
        self.highscore = self.get_highscore()
        self.current_score = 0

    def add_score(self, amount):
        self.current_score += amount
        if self.is_highscore(self.current_score):
            self.overwrite_highscore(self.current_score)
    
    def reset_score(self):
        self.current_score = 0
    
    def is_highscore(self, score):
        return score > self.highscore

    def get_highscore(self):
        file = open("scores.txt", "r")
        score = file.read()
        return int(score)

    def overwrite_highscore(self, score):
        self.highscore = score
        file = open("scores.txt", "w")
        file.write(str(score))

    def get_topten(self):
        return None
    
    def get_user_highscore(self, username):
        return None
    
    def add_score_to_database(self, username):
        pass

    