def recurPowerNew(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    elif exp % 2 !=0:
        return base * recurPowerNew(base, exp-1)
    elif exp % 2 == 0:
        return recurPowerNew(base*base,exp/2)
        
    
