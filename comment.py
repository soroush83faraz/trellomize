import datetime

class Comment :
    name = None
    time = None
    text = None
    def __init__(self , name = "User" , time = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S") , text = "my comment" ):
        self.name = name
        self.time = time
        self.text = text
    def converting_to_str (self) :
        return str(self.text + '\n' + self.name + '\n' + self.time)

    
from datetime import *


class Commento:
    writer = None
    date = None
    content = None

    def __init__(self , writer):
        self.writer = writer

    def make_dict_of_comments(self):
        dictionary = {'Writer' : self.writer , 'Date' : self.date , 'Content' : self.content}
        return dictionary
    
