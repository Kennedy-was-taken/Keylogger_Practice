import files 
import datetime

class Control_Keys:
    
    erased_word = []
    deleted_word =[]
    
    def __init__(self):
        pass
    
    # every time the enter key is pressed
    def enter_Key(self,Key):
        key = files()
        key.write_file("/n", Key)
    
    @classmethod
    def backspace_Key(key_word):
        global erased_word
        erased_word.append(str(key_word))
    
    @classmethod
    def delete_Key(key_word):
        global deleted_word
        deleted_word.append(str(key_word))
    
    if "__main__" == __name__:
        pass