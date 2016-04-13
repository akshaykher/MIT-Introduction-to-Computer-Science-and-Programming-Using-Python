def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    
    ('I', 'am', 'a', 'test', 'tuple')
    ('I', 'a', 'tuple')
    '''
    # Your Code Here
    output = ()         
    length = len(aTup)
    for i in range(length):
        if i%2 == 0:
            output = output + (aTup[i],)
    return output
    
