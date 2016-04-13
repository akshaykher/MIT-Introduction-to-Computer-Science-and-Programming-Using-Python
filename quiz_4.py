"""
Write a Python function that returns True if aString is a palindrome (reads the same forwards or reversed) and False otherwise. 
Do not use Python's built-in reverse function or aString[::-1] to reverse strings.
"""
def isPalindrome(aString):
    '''
    aString: a string
    '''
    result = True
    i=0
    length = len(aString)
    counter = length/2
    while(i<counter):
        result = result and aString[i]==aString[(length-1)-i]
        i=i+1
    return result
    
def isPalindrome(aString):
    pal=""
    i = len(aString)-1
    while i>=0:
        pal = pal + aString[i]
        i = i-1
    return pal == aString