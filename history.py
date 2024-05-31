


class History():
    
    """
    Represents historical events.

    Attributes:
        doer (str): The person or entity associated with the event.
        date (str): The date when the event occurred.
        content (str): A brief description of the historical content.

    Methods:
        make_dict_of_history(): Returns a dictionary representation of the history.

    """    


    doer = None
    date = None
    content = None

    def __init__(self):
        pass

    def make_dict_of_history(self):
        
        """
        Returns a dictionary containing history details.

        Returns:
            dict: A dictionary with keys 'Doer', 'Date', and 'Content'.
        """
        
        dicted = {'Doer' : self.doer , 'Date' : self.date , 'Content' : self.content}
        return dicted