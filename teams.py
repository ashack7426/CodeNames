class Team:
    def __init__(self,color):
        self.color = color
        self.__words = []
        self.__shown = {}
    
    def addWords(self,words):
        self.__words = words
        for w in words:
            self.__shown[w] = False
    
    def getWords(self):
        return self.__words
    
    def showWord(self,word):
        if word in self.__words:
            self.__shown[word] = True
    
    def iswordShown(self, word):
        return self.__shown[word]
    
    def wordsLeft(self):
        left = []

        for w,shown in self.__shown.items():
            if not shown:
                left.append(w)
        
        return left

