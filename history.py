


class History():

    doer = None
    date = None
    content = None

    def __init__(self):
        pass

    def make_dict_of_history(self):
        dicted = {'Doer' : self.doer , 'Date' : self.date , 'Content' : self.content}
        return dicted