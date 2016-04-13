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
        

            
    
