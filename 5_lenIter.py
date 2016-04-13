def lenIter(aStr):
    i = 0
    check =" "
    while(True):
        try:
            check = aStr[i]
            i = i+1
        except IndexError:
            length = i
            break
    return length
