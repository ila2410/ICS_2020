#This project is a retatively simple hangman game in one class.
import random

class HangMan(object):
    
    # Game set up.
    hang = []
    hang.append(' +---+')
    hang.append(' |   |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('=======')

    # Hangman body
    man = {}
    man[0] = [' 0   |']
    man[1] = [' 0   |', ' |   |']
    man[2] = [' 0   |', '/|   |']
    man[3] = [' 0   |', '/|\\  |']
    man[4] = [' 0   |', '/|\\  |', '/    |']
    man[5] = [' 0   |', '/|\\  |', '/ \\  |']
    
    pics = []
    
    words = ['alligator','bear','camel','cat','cheetah','chimpanzee','cow','crocodile', 'deer', 'dog',
'elephant', 'fox', 'giraffe', 'goat', 'hamster', 'horse', 'kangaroo', 'lion', 'monkey', 'panda', 'pig', 'rabbit', 'rat', 
'seal', 'sheep', 'squirrel', 'tiger', 'wolf', 'zebra'
]
  #defenitions

    def __init__(self, *args, **kwargs):
        i, j = 2, 0
        self.pics.append(self.hang[:])
        for ls in self.man.values():
            pic, j = self.hang[:], 0
            for m in ls:
                pic[i + j] = m
                j += 1
            self.pics.append(pic)

    def print_opening_words(self):
        print('Welcome to a game of hangman!')
        print('Hint!!! All words are animals.')
        print('Good luck!')

    def pickWord(self):
        return self.words[random.randint(0, len(self.words) - 1)]
    
    def printPic(self, idx, wordLen):
        for line in self.pics[idx]:
            print(line)
            
    def askAndEvaluate(self, word, result, missed):
        guess = input()
        if guess == None or len(guess) != 1 or (guess in result) or (guess in missed):
            return None, False
        i = 0
        right = guess in word
        for c in word:
            if c == guess:
                result[i] = c
            i += 1
        return guess, right

    def info(self, info):
        print(info)  
          
    def start(self):
        self.print_opening_words()

        word = list(self.pickWord())
        result = list('_' * len(word))
        success, i, missed = False, 0, []

        print('The word has _ characters: ', result)

#main loop of the game.

        while i < len(self.pics)-1:
            print('Guess a letter: ', end='')
            guess,right = self.askAndEvaluate(word, result, missed)
            if guess == None:
                print('You\'ve already entered this character.')
                continue
            print(''.join(result))
            if result == word:
                self.info('Congratulations! You win!')
                success = True
                break
            if not right:
                missed.append(guess)
                i+=1
            self.printPic(i, len(word))
            print('Guessed characters: ', missed)
        
        if not success:
            self.info('The word was \''+''.join(word)+'\'!')
            print('You diet!')
            print('Try again.')
           
a = HangMan().start()