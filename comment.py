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
    
