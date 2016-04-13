def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if secretWord[-1:] == '':
        return True
    elif not(secretWord[-1:] in lettersGuessed):
        return False
    else:
        return True and isWordGuessed(secretWord[:-1],lettersGuessed)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    secretWord = 'apple' 
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    '''
    append=""
    # FILL IN YOUR CODE HERE...
    if secretWord[-1:] == '':
        return ""
    elif secretWord[-1:] in lettersGuessed:
        append = secretWord[-1:]
        return getGuessedWord(secretWord[:-1],lettersGuessed) + append
    elif not(secretWord[-1:] in lettersGuessed):
        append = "_"
        return getGuessedWord(secretWord[:-1],lettersGuessed) + append
        
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    print getAvailableLetters(lettersGuessed)
    abcdfghjlmnoqtuvwxyz
    '''
    import string
    not_guessed = string.ascii_lowercase
    for i in lettersGuessed:
        if i in not_guessed:
            not_guessed = not_guessed.replace(i,"")
    return not_guessed
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guess = 8
    anyletter =""
    lettersGuessed = ""
    lettersGuessedWrong = ""
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print("-------------")
    while guess >0:
        print("You have " + str(guess) + " guesses left.")
        print("Available letters: " + getAvailableLetters(anyletter))
        user_data = raw_input('Please guess a letter: ').lower()
        if user_data in lettersGuessed or user_data in lettersGuessedWrong:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        elif user_data in secretWord:
            lettersGuessed = lettersGuessed + user_data
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print("-------------")
                break
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessedWrong = lettersGuessedWrong + user_data
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            guess = guess - 1
        anyletter = anyletter + user_data
   	print("-------------")
    if guess == 0:
        return("Sorry, you ran out of guesses. The word was " + secretWord + ".")
    else:
        return("Congratulations, you won!")
