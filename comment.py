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

    