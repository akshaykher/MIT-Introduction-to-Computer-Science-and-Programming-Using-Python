#nfruits({'D': 7, 'F': 9, 'I': 10, 'J': 6, 'L': 9, 'P': 9, 'S': 7, 'W': 7, 'X': 9}, 'P') ->10
#nfruits({'I': 9, 'X': 7, 'K': 9, 'M': 10, 'S': 5}, 'XM') ->10
#nfruits({'A': 1, 'B': 2, 'C': 3},'AC') ->3

#names = x.keys()
#[x[i] for i in names]


def nfruits(dictn,string):
    length_string = len(string)
    for i in range(length_string):
        if(i<length_string-1):
            dictn.update((x,y+1) for x,y in dictn.items())
            dictn[string[i]] -=2
            print(dictn)
        else:
            dictn[string[i]] -=1
            print(dictn)
    print(dictn)
    return max(dictn.values())
            
    
