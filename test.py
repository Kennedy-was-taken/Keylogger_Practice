with open('log.txt', 'r') as file:
    something = file.read()
    print(something[-1])
    
    def readfile():
        with open('log.txt', 'r') as f:
            lastCharacter = f.read()
            
        if(lastCharacter[-1] == ' '):
            return True
        else:
            return False
