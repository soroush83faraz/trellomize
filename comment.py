from datetime import *

class Commento:
    writer = None
    time = None
    text = None
    def __init__(self , writer = "User" , time = datetime.now().strftime("%Y-%m-%d  %H:%M:%S") , text = "my comment" ):
        self.writer = writer
        self.time = time
        self.text = text
    def converting_to_dictionary (self) :
        return {'Writer' : self.writer , 'Text' : self.text , 'Time' : self.time}

    


