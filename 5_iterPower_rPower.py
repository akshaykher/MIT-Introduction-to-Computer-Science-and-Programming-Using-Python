def iterPower(base, exp):
    result = 1
    i = 1
    while i <= exp:
        result = result * base
        i = i+1
    return result
    
def recurPower(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)
    