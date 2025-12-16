class student:
    def __init__(self,name,scores):
        self.name = name
        self.score = scores
    
    def average (self):
        if self.score == 0:
            return 'ERORR...you are Zero!'
        average = (self.score) / len(self.score)
        return average
    
    def state (self):
        state = self.average
        if state >= 17:
            return 'very good'
        elif 12 <= state < 17:
            return 'okey'
        else:
            return 'very bad'


