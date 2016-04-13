animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    count = 0
    key = ''
    if len(aDict.keys()) == 0 and len(aDict.values()) == 0:
        return None
    else:
        for i in aDict.keys():
            if len(aDict[i]) > count:
                count = len(aDict[i])
                key = i
        if key == '':
            return aDict.keys()[0]
        else:
            return key

#biggest({})
#biggest({'o': []})
len(aDict.keys())
len(aDict.values())