#import string
#print string.ascii_lowercase

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
