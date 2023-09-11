# importing pynput to use its functions to capture key inputs
import pynput
from pynput.keyboard import Key, Listener

from files import write_Read
from specialKeys import Control_Keys
from datetime import datetime


# Every time the key gets pressed
def on_press(key):

    print("{0} key was pressed".format(key))
    if key == str(Key.enter):
        # calls the enter_key method from the specialKeys.py
        control_key.enter_Key(Key)

    else:
        # calls the write_file method from the files.py
        pressed_key.write_file(key, Key)

# breaks out of the loop
def on_release(key):
    if key == Key.esc:
        isStarted = False
        return False

#Captures the time taken 
def captured_time():
    if isStarted == True:
        current_Time = datetime.now()
        pressed_key.time_Start(current_Time.strftime("%Y-%m-%d %H:%M:%S"))
    elif isStarted == False:
        current_Time = datetime.now()
        pressed_key.time_end(current_Time.strftime("%Y-%m-%d %H:%M:%S"))

if ('__main__' == __name__):
    control_key = Control_Keys()
    pressed_key = write_Read()
    isStarted = True
    current_Time = ""
    captured_time()
    # with Listener(on_press=on_press, on_release=on_release) as listener:
    #     listener.join()
