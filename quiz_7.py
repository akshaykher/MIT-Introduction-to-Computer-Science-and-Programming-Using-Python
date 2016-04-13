d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
def f(a,b):
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here


    dict1 = {}
    x = d1.keys()
    y = d2.keys()
    k = []
    for i in range(len(x)):
        if x[i] in y:
            k.append(x[i])
    for i in range(len(k)):
        dict1[k[i]] = f(d1[k[i]],d2[k[i]])
    
    dict2 = {} 
    x = d1.keys()
    y = d2.keys()  
    k1 = []
    k2 = []
    for i in range(len(x)):
        if not(x[i] in y):
            k1.append(x[i])
            
    for i in range(len(y)):
        if not(y[i] in x):
            k2.append(y[i])
    
    for i in range(len(k1)):
        dict2[k1[i]] = d1[k1[i]]
    for i in range(len(k2)):
        dict2[k2[i]] = d2[k2[i]]
        
    return (dict1,dict2)