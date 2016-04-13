"""
Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
  #
counter = 0
def flat(lst):
    global counter
    counter = counter+1
    print "counter", counter
    l = len(lst)
    temp = []
    for i in range(l):
        if type(lst[i]) == list:
            temp1 = flat(lst[i])
            temp.append(temp1)
        else:
            temp.append(str(lst[i]))
    return temp
    