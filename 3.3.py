l = [56 ,9 ,11 ,2 ]

def renumb(y):
    
    string = ''
    y.sort(key=lambda x: str(x)[0], reverse = True)
    for i in y:
        string += str(i)
    print(string)
renumb(l)