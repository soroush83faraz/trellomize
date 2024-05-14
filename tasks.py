import datetime
#Function to making unique ID for our task using uuID library======
def make_unique_ID():
    pass


#==================================================================

class Task:
    ID = None
    title = None
    discription = None
    start_time = None
    end_time = None
    assignees = []
    priority = None
    status = None
    history = None
    comments  = []

    def __init__(self , title):
        self.title = title
        self.start_time = (datetime.datetime.now()).strftime("%Y-%m-%d   %H")
        self.end_time = self.start_time + datetime.timedelta(hours=24)
        self.ID  = make_unique_ID()