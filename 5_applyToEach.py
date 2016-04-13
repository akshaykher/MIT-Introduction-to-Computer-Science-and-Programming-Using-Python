# Your Code Here
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    print(L)
        
applyToEach(testList,abs)

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = L[i] + f
    print(L)
    
applyToEach(testList, 1)

# Your Code Here
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = L[i]**f
    print(L)
    
applyToEach(testList, 2)