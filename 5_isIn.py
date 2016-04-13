def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    aStr = sorted(aStr)
    if aStr[len(aStr)/2] == char:
        return True
    elif len(aStr) == 1:
        return False
    low = 0
    high = len(aStr) - 1
    middle = (high + low)/2
    if char < aStr[middle]:
        #low = low
        high = middle
    else:
        low = middle
        #high = high
    if len(aStr) == 2:
        return False or isIn(char, aStr[low:high])
    else:
        return False or isIn(char, aStr[low:high+1])
   
""" 
aStr = 'akshay'
char = 'x'
low = 0
high = len(aStr) - 1
middle = (high + low)/2
aStr = aStr[low:high+1]
"""
