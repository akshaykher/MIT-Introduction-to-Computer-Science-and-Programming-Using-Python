#def lenRecur(aStr):
#    check = 0
#    if aStr == '':
#        return 0               
#    else:
#        try:
#            check = aStr[1]
#        except IndexError:
#            return 1
#        return 2 + lenRecur(aStr[1:-1])

def lenRecur(aStr):
    check = 0
    if aStr == '':
        return 0               
    else:
        return  1 + lenRecur(aStr[0:-1])