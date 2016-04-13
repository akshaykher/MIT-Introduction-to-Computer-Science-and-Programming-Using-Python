def gcdIter(a,b):
    hcf = 1
    if a<b:
        value = a
    else:
        value = b
    while(value > 1):
        if a%value == 0 and b%value == 0:
            hcf = value
            break
        value = value - 1
    return hcf
    
    