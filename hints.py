class Hint:
    def __init__(self,hint, hint_num, words,value, source):
        self.hint = hint
        self.hint_num = hint_num
        self.words = words
        self.value = value
        self.source = source
    

    def __lt__(self,other):
        if self.value == other.value:
            return self.hint_num < other.hint_num
        return self.value < other.value
    

    def __repr__(self):
        return "(" + self.hint + "," + str(self.hint_num) + "," + str(self.words) + "," + str(self.value) + ", " + self.source + ")"

    