from datetime import *

class Commento:
    
    """
    Represents a comment with information about the writer, time, and text.

    Attributes:
        writer (str): The name of the person who wrote the comment.
        time (str): The timestamp when the comment was created.
        text (str): The content of the comment.

    Methods:
        converting_to_dictionary(): Converts the comment object to a dictionary.

    """
    
    writer = None
    time = None
    text = None
    def __init__(self , writer = "User" , time = datetime.now().strftime("%Y-%m-%d  %H:%M:%S") , text = "my comment" ):
        self.writer = writer
        self.time = time
        self.text = text
    def converting_to_dictionary (self) :
        
        """
        Converts the comment object to a dictionary.
        
        Returns:
            dict: A dictionary containing comment details.
        """
        return {'Writer' : self.writer , 'Text' : self.text , 'Time' : self.time}

    


