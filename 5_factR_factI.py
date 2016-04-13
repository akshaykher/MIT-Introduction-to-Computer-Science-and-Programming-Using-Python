#iterative factorial
def factI(a):
    result = 1
    while(a >=1):
        result = result * a
        a = a-1
    return result

#recursive factorial
def factR(a):
    if a == 1:
        return a
    else:
        return a * factR(a-1)
