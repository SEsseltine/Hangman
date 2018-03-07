import random

file = open('wordBank.txt','r')
word_bank = file.read().splitlines()


def chooseWord():
    print('Choosing a word...')
    return random.choice(word_bank).replace(' ','')

def gameScreen(gC,bW,pG):
    print('\n','-=-'*2,'HANGMAN','-=-'*2)
    print(bW)
    print('Wrong Guesses:',gC,'/ 10')
    print('Past Guesses:', ', '.join(pG))

def guessValidate(guess, pastGuesses):
    if len(guess) > 1:
        print('Your guess can only be one character')
    elif guess in pastGuesses:
        print('You already guessed that!')
    elif not guess.isalpha():
        print('You can only guess letters')
    else:
        return True
    return False


def changeChar(string, index, char):
    string = string[:index] + char + string[index+1:]
    return string

def blankWordUpdate(bW,sW,guess):
    for i in range(len(sW)):
        if sW[i] == guess.lower():
            bW = changeChar(bW,i*2,guess.lower())
        elif sW[i] == guess.upper():
            bW = changeChar(bW,i*2,guess.upper())
    return bW
        
        


def game():
    print('Starting a new game...')

    # Initialize variables
    guessCount = 0
    pastGuesses = []
    secretWord = chooseWord()
    blankWord = '_ '*len(secretWord)

    while '_' in blankWord and guessCount < 10:
        gameScreen(guessCount, blankWord, pastGuesses)

        # Let the user make a guess
        guess = input('Your guess: ').lower()
        while not guessValidate(guess, pastGuesses):
            guess = input('Your guess: ')

        # Add their guess to the list of past guesses
        pastGuesses.append(guess)

        if guess in secretWord.lower():
            blankWord = blankWordUpdate(blankWord,secretWord,guess)
        else:
            guessCount += 1

    
    if '_ ' in blankWord:
        gameScreen(guessCount, blankWord, pastGuesses)
        print('loser.')
        print('The word was:',secretWord)
    else:
        gameScreen(guessCount, blankWord, pastGuesses)
        print('GAME OVER')
        print('WINNER WINNER')

    
    if input('Type "PLAY" to play again! ').lower() == 'play':
        game()
    else:
        quit()


print('Hello!  Welcome to hangman!')
input('Press the RETURN key to get started...')
game()
