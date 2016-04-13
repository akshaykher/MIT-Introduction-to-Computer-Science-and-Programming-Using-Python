L = ['a', 'b', 'a']

def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    for i in range(len(L)):
        if not (f(L[i])):
            del L[i]
    return len(L)
    
L = ['a', 'b', 'a']
print satisfiesF(L)
print L