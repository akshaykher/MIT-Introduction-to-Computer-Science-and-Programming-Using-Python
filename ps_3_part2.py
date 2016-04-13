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