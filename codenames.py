
from game import Game
import pygame, sys
from pygame.locals import *
#import requests
import random
import gensim
import itertools
from hints import Hint



import re
regex = re.compile('[^a-z]')


import inflect

import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
import wikipedia


#Additional words that need to be removed
removedWords = ["besides", "also", "likewise", "too", "aswell", "st", "th", "i", "ane" \
				"may", "many", "one", "new", "two", "first", "use", "used", "known", \
				"however", "often", "including", "three"]

stopWords = ["0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "A", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "after", "afterwards", "ag", "again", "against", "ah", "ain", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appreciate", "approximately", "ar", "are", "aren", "arent", "arise", "around", "as", "aside", "ask", "asking", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "B", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "been", "before", "beforehand", "beginnings", "behind", "below", "beside", "besides", "best", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "C", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "ci", "cit", "cj", "cl", "clearly", "cm", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "could", "couldn", "couldnt", "course", "cp", "cq", "cr", "cry", "cs", "ct", "cu", "cv", "cx", "cy", "cz", "d", "D", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "dj", "dk", "dl", "do", "does", "doesn", "doing", "don", "done", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "E", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "F", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "G", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "H", "h2", "h3", "had", "hadn", "happens", "hardly", "has", "hasn", "hasnt", "have", "haven", "having", "he", "hed", "hello", "help", "hence", "here", "hereafter", "hereby", "herein", "heres", "hereupon", "hes", "hh", "hi", "hid", "hither", "hj", "ho", "hopefully", "how", "howbeit", "however", "hr", "hs", "http", "hu", "hundred", "hy", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "im", "immediately", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "inward", "io", "ip", "iq", "ir", "is", "isn", "it", "itd", "its", "iv", "ix", "iy", "iz", "j", "J", "jj", "jr", "js", "jt", "ju", "just", "k", "K", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "ko", "l", "L", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "M", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "my", "n", "N", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "neither", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "O", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "otherwise", "ou", "ought", "our", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "P", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "pp", "pq", "pr", "predominantly", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "Q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "R", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "S", "s2", "sa", "said", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "seem", "seemed", "seeming", "seems", "seen", "sent", "seven", "several", "sf", "shall", "shan", "shed", "shes", "show", "showed", "shown", "showns", "shows", "si", "side", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somehow", "somethan", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "sz", "t", "T", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "thereof", "therere", "theres", "thereto", "thereupon", "these", "they", "theyd", "theyre", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "U", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "used", "useful", "usefully", "usefulness", "using", "usually", "ut", "v", "V", "va", "various", "vd", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "W", "wa", "was", "wasn", "wasnt", "way", "we", "wed", "welcome", "well", "well-b", "went", "were", "weren", "werent", "what", "whatever", "whats", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "whom", "whomever", "whos", "whose", "why", "wi", "widely", "with", "within", "without", "wo", "won", "wonder", "wont", "would", "wouldn", "wouldnt", "www", "x", "X", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "Y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "your", "youre", "yours", "yr", "ys", "yt", "z", "Z", "zero", "zi", "zz"]

model = gensim.models.KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin', binary=True, limit=500000)
    

def getWikiWords(words, num):
    word_freq = {}

    for w in words:
        wordPages = wikipedia.search(w)

        for i in wordPages:
            page = wiki_wiki.page(i)

            if page.exists():
               words_pres = page.text.split()

               for currWord in words_pres:
                   currWord = currWord.lower()

                   if ' ' not in currWord:
                        currWord = regex.sub('', currWord)

                        if(currWord):
                            if currWord in word_freq:
                                word_freq[currWord] += 1
                            else:
                                word_freq[currWord] = 1
        
    
    for removalWord in removedWords + stopWords:
        if removalWord in word_freq.keys():
            del word_freq[removalWord]
    
    if "may" in word_freq:
        del word_freq["may"]
    


	
	#Remove the word itself
    word_freq = {k:v for k,v in word_freq.items() if k not in words}


    #Get Top 20 words
    word_lst = sorted(word_freq, key=word_freq.get, reverse=True)

    cnt = 0
    freq = {}
    total = 0
    while cnt < min(num, len(word_lst)):
        for w in word_lst:
            freq[w] = word_freq[w]
            cnt += 1
            total += word_freq[w]

            if cnt == num:
                break


    
    #Return (word,value)
    lst = []

    for k,v in freq.items():
        lst.append((k,v / total, "wiki"))

    return lst



""" 
def genWordList():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    f = open("rand_word_list.txt", "w+")

    for w in WORDS:
        f.write(str(w)[2:len(str(w)) - 1])
        f.write('\n')

    f.close() """


def readWordList():
    lst = []


    """ f = open("rand_word_list.txt", "r+")
    words = f.readlines()

    for w in words:
        lst.append(w[:len(w) - 1])
    f.close() """

    f = open("codenames_words.txt", "r+")
    words = f.readlines()

    for w in words:
        w = w.lower()

        if w not in lst:
            lst.append(w[:len(w) - 1])
            
    f.close()

    return lst



def validWord(ww, game):
    valid = True
    engine = inflect.engine()

    if '_' in ww:
        valid = False

    for w in game.getAllWords():
        if engine.plural(w) == ww or engine.plural(ww) == w or w in ww or ww in w:
            valid = False
            break

    return valid

    

def getWikiDict(positive_words):
    positive_word_wiki_word_freq = {}


    for w in positive_words:
        wordPages = wikipedia.search(w)
        word_freq = {}

        for i in wordPages:
            page = wiki_wiki.page(i)

            if page.exists():
                words_pres = page.text.split()

                for currWord in words_pres:
                    currWord = currWord.lower()

                    if ' ' not in currWord:
                        currWord = regex.sub('', currWord)

                        if(currWord):
                            if currWord in word_freq:
                                word_freq[currWord] += 1
                            else:
                                word_freq[currWord] = 1
            

    
        for removalWord in removedWords + stopWords:
            if removalWord in word_freq.keys():
                del word_freq[removalWord]
    
        if "may" in word_freq:
            del word_freq["may"]
    

	    #Remove the word itself
        word_freq = {k:v for k,v in word_freq.items() if k not in positive_words}

        positive_word_wiki_word_freq[w] = word_freq



    return positive_word_wiki_word_freq




def getPositiveWikiWords(positive_words, num,postive_wiki_dict ):
    all_dict = {}

    for p in positive_words:
        word_freq = postive_wiki_dict[p]

        for k,v in word_freq.items():
            if k in all_dict.keys():
                all_dict[k] += v
            else:
                 all_dict[k] = v
    

    #Get Top 20 words
    word_lst = sorted(all_dict, key=all_dict.get, reverse=True)

    cnt = 0
    freq = {}
    total = 0
    while cnt < min(num, len(word_lst)):
        for w in word_lst:
            freq[w] = all_dict[w]
            cnt += 1
            total += all_dict[w]

            if cnt == num:
                break


    #Return (word,value)
    lst = []

    for k,v in freq.items():
        lst.append((k,v / total, "wiki"))

    return lst




def getBotHint(game):
    possible_hints = []
    engine = inflect.engine()

    positive_words = []
    negative_words = []

    turn = game.getTurn()
    blue_words = game.blue.wordsLeft()
    red_words = game.red.wordsLeft()
    black = game.black
   


    if turn == "Blue":
        positive_words = blue_words
        negative_words = red_words + [black]
    else:
        positive_words = red_words
        negative_words = blue_words + [black]

    p = []
    for word in positive_words:
        try:
            model.most_similar(positive = word)
            p.append(word)
        except:
            continue
    
    positive_words = p

    n = []
    for word in negative_words:
        try:
            model.most_similar(negative = word)
            n.append(word)
        except:
            continue
    
    negative_words = n

    #Go From top to bottom 
    #start with len(positive words) then go to 1
    #remove all words with mu

    if(len(positive_words) and len(negative_words)):
        print(positive_words)
        print(negative_words)

        cnt = min(4,len(positive_words))

        print("Wikipedia Words............")
        negative_wiki_words = getWikiWords(negative_words,10)
        
        postive_wiki_dict = getWikiDict(positive_words)

     
        print("Word2vec Words............")
        while cnt > 1:

            combos = itertools.combinations(positive_words, cnt)
            

            for c in combos:
                positive_wiki_words = getPositiveWikiWords(c,10,postive_wiki_dict )

                for i in range(len(positive_wiki_words)):
                    (x, xv, source) = positive_wiki_words[i]

                    for (xx, xxv,source) in negative_wiki_words:
                        if xx == x:
                            positive_wiki_words[i] = (x,xv - xxv,source)
                            break

                lst = model.most_similar(
                positive=c,
                negative=negative_words,
                restrict_vocab=50000)

                ll = []
                for (x,y) in lst:
                    ll.append((x.lower(),y,"word2vec"))
                
                lst = ll
                lst = positive_wiki_words + lst

                # hint, hint num, subset of words, cosine number 
                for (ww,vv,source) in lst:
                    #make sure all words are just one word no word with _ and none of words are any of words on board
                    if validWord(ww,game):
                        h = Hint(ww,cnt,c,vv,source)
                        if len(possible_hints) < 10:

                            found = False
                            for hh in possible_hints:
                                if hh.hint == ww or hh.hint == engine.plural(ww) or ww == engine.plural(hh.hint):
                                    if vv > hh.value:
                                        possible_hints.remove(hh)
                                        possible_hints.append(h)

                                    found = True
                                    break
                            
                            if not found:
                                possible_hints.append(h)


                        else:
                            for hh in possible_hints:
                                if vv > hh.value:
                                    possible_hints.remove(possible_hints[-1])

                                    found = False
                                    for hh in possible_hints:
                                        if hh.hint == ww or hh.hint == engine.plural(ww) or ww == engine.plural(hh.hint):
                                            if vv > hh.value:
                                                possible_hints.remove(hh)
                                                possible_hints.append(h)
            
                                            found = True
                                            break
                                    
                                    if not found:
                                        possible_hints.append(h)
                                    
                                    break
                        
                        possible_hints.sort(reverse=True)

            cnt -= 1
    
    for p in possible_hints:
        print(p)
    return possible_hints[0].hint, possible_hints[0].hint_num

   
def get_word_from_mouse(pos, game):
    x,y = pos


    #Get Col
    #x is between (220, 420) = 0
    #x is between (440, 640) = 1
    #x is between (660, 860) = 2
    #x is between (880, 1080) = 3
    #x is between (1100, 1300) = 4

    if x >= 220 and x <= 420:
        col = 0
    elif x >= 440 and x <= 640:
        col = 1
    elif x >= 660 and x <= 860:
        col = 2
    elif  x >= 880 and x <= 1080:
        col = 3
    elif x >= 1100 and x <= 1300:
        col = 4
    else:
        col = None

    #Get Row
    #y is betwwen (40,140)
    #y is betwwen (160, 260)
    #y is betwwen (280, 380)
    #y is betwwen (400, 500)
    #y is betwwen (520, 620)

    if y >= 40 and y <= 140:
        row = 0
    elif y >= 160 and y <= 260:
        row = 1
    elif y >= 280 and y <= 380:
        row = 2
    elif y >= 400 and y <= 500:
        row = 3
    elif  y >= 520 and y <= 620:
        row = 4
    else:
        row = None

   
    print(row,col)
    if(row != None and col != None):
        cnt = row * 5 + col
        return game.getAllWords()[cnt]
    else:
        return None



def setup():
    all_words = []
    starting_words = []
    other_words = []
    neutrals = []

    team = int(input("What Team are you on Blue(0) or Red(1)? "))
    starting = int(input("Are you going first? (yes = 1 and no = 0)? "))

    if starting:
        cnt = 9
    else:
        cnt = 8

    print()
    rand_words = int(input('Do you want random words(yes = 1 and no = 0)? '))

    if rand_words:
        i = 0
        all_words = random.sample(readWordList(),25)

        #Starting Words
        for _ in range(9):
            starting_words.append(all_words[i])
            i += 1
        
        #Other Words
        for _ in range(8):
            other_words.append(all_words[i])
            i += 1

        #Neutral Words
        for _ in range(7):
            neutrals.append(all_words[i])
            i += 1
        
        black = all_words[i]
        

    else:
        word_num = 1
        while(len(starting_words) < cnt):
            word = input("What is your word " + str(word_num) + "? ")
            if word not in starting_words:
                starting_words.append(word)
                word_num += 1
        
        
        all_words += starting_words

        if cnt == 8:
            cnt = 9
        else:
            cnt = 8

        print()
        word_num = 1
        while(len(other_words) < cnt):
            word = input("What is your opponent's word " + str(word_num) + "? ")
            if word not in other_words and word not in all_words:
                other_words.append(word)
                word_num += 1
        
        all_words += other_words
        print()
        word_num = 1
        while(len(neutrals) < 7):
            word = input("What is bystander word " + str(word_num) + "? ")
            if word not in neutrals and word not in all_words:
                neutrals.append(word)
                word_num += 1
        

        all_words += neutrals

        print()
        black = input("What is the assassin word? ")

        while black in all_words:
            black = input("What is the assassin word? ")

    if team == 1:
        red = starting_words
        blue = other_words
    else:
        red = other_words
        blue = starting_words

    game = Game(black, neutrals,red,blue)
    print()
    return game



def playGame():
    play = True
    pygame.init()
    font = pygame.font.SysFont('Arial', 35)

    while play:
        game = setup()
        gameOver = False

        while not gameOver:
            turn = game.getTurn()

            if turn == "Blue":
                word_color = (0,0,204)
            else:
                word_color = (204,0,0)

            turn_txt = font.render(turn + " Turn!", True, word_color)
            game.drawGame(gameOver, turn_txt)
          

            #Replace Hint with AI Chosen Hint 
            bot_hint = input("Do you want to use the Bot Hint? (yes = 1 and no = 0)? ")

            if bot_hint:
                turn_txt = font.render("Generating Bot Hint..............", True, word_color)
                game.drawGame(gameOver, turn_txt)
                hint, hint_num = getBotHint(game)
            else:
                hint = input("What is your hint word? ")

                while hint in game.getAllWords():
                    print("Hint cannot be a word in the list")
                    hint = input("What is your hint word? ")

                hint_num = int(input("what is your hint num? "))


            #Display Hint on Screen
            guess_num = 0
            turnOver = False


            if turn == "Blue":
                word_color = (0,0,204)
            else:
                word_color = (204,0,0)


            keep_going = True
            hint_txt = font.render(hint + ", " + str(hint_num), True, word_color)
            

            while(not turnOver):
                game.drawGame(gameOver, hint_txt)

                if guess_num == hint_num:
                    keep_going = int(input("Do you want to keep guessing? (yes = 1 and no = 0)? "))

                if(not keep_going):
                    turnOver = True
                    break
                
                #Replace this with just clicking the word tile 
                #First thing to do is to get mouse position 
                #Somehow connect mouse pos to the letter on screen
                #On click choose that word 

                word = None
                while not word:
                    for event in pygame.event.get():
                        pos = pygame.mouse.get_pos()
                        w = get_word_from_mouse(pos, game)
                        print(w)

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if w and not game.isWordShown(w):
                                word = w
                                break
                
                color = game.getWordColor(word)
                guess_num += 1
                game.drawGame(gameOver, hint_txt)


                if color == "BL":
                    turnOver = True
                    gameOver = True
                elif color != turn or game.cardsLeftNum(turn) == 0 or guess_num == hint_num + 1:
                    turnOver = True
                

            
            #Current Team chose the assassin
            if gameOver:
                game.changeTurns()
                #turn is the winner
                turn = game.getTurn()
                print(turn + " Team Wins!")
                break
            
            if game.cardsLeftNum(turn) == 0:
                gameOver = True
                #turn is the winner
                print(turn + " Team Wins!")
                break
            
            game.changeTurns()


        if turn == "Blue":
            word_color = (0,0,204)
        else:
            word_color = (204,0,0)

        gameOver_txt = font.render(turn + " Team Wins!", True, word_color)
        
        game.drawGame(gameOver, gameOver_txt)
        choice = int(input("Do you want to play again(1) or Quit(0)? "))
        
        if choice == 0:
            play = False

   
       
def main():
    playGame()


if __name__ == "__main__":
    main()
