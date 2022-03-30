from teams import Team
import random
import pygame
from pygame.locals import *

class Game:
    def __init__(self, black, neutral, red, blue):
        self.black = black

        self.blue = Team("B")
        self.blue.addWords(blue)
        
        self.red = Team("R")
        self.red.addWords(red)

        self.neutral = Team("N")
        self.neutral.addWords(neutral)

        if len(self.blue.getWords()) > len(self.red.getWords()):
            self.turn = "B"
        else:
            self.turn = "R"
        
        self.all_words = [black] + self.blue.getWords() + self.red.getWords() + self.neutral.getWords()
        random.shuffle(self.all_words)

        self.display = pygame.display.set_mode((1500,800))

    
    def getWordColor(self,word):
        if word == self.black:
            return "BL"
        elif word in self.neutral.getWords():
            self.neutral.showWord(word)
            return "N"
        elif word in self.red.getWords():
            self.red.showWord(word)
            return "Red"
        elif word in self.blue.getWords():
             self.blue.showWord(word)
             return "Blue"
        else:
            return None
    
    def getDisplay(self):
        return self.display
          
    def cardsLeftNum(self, team):
        if team == "Red":
            return len(self.red.wordsLeft())
        elif team == "Blue":
            return len(self.blue.wordsLeft())
    
    def isWordShown(self,word):
        if word in self.blue.getWords():
           return self.blue.iswordShown(word)
        elif word in self.neutral.getWords():
            return self.neutral.iswordShown(word)
        elif word in self.red.getWords():
            return self.red.iswordShown(word)
    

    def changeTurns(self):
        if self.turn == "B":
            self.turn = "R"
        else:
            self.turn = "B"

    def getTurn(self):
        if self.turn == "B":
            return "Blue"
        else:
            return "Red"
    
    def getAllWords(self):
        return self.all_words

    def drawGame(self, gameOver, txt):


        #make a rectangle with light green background (board)
        self.display=pygame.display.set_mode((1400,800))
        GREY=(128,128,128)
        self.display.fill(GREY)

        cnt = 0
        font = pygame.font.SysFont('Arial', 25)

        y = 40
        for _ in range(5):
            x = 160
            for _ in range(5):
                
                word_color = (0,0,0)
                if self.isWordShown(self.all_words[cnt]) or gameOver:
                    word_color = (255,255,255)

                    if self.getWordColor(self.all_words[cnt]) == "BL":
                        color = (0,0,0)
                    elif self.getWordColor(self.all_words[cnt]) == "N":
                        color = (139,70,0)
                    elif self.getWordColor(self.all_words[cnt]) == "Blue":
                        color = (0,139,139)
                    elif self.getWordColor(self.all_words[cnt]) == "Red":
                        color = (139,0,0)

                else:
                    color = (255,255,255)


                word = font.render(self.all_words[cnt], True, word_color)
                pygame.draw.rect(self.display, color, (x,y, 200, 100))
                self.display.blit(word,  (x + 10, y + 30))
                x += 220
                cnt += 1
            y += 120

        if txt:
            self.display.blit(txt,  (600, y + 30))
        pygame.display.update()


     
    

