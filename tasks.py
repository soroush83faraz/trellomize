import datetime
import uuid
from enum import Enum
from datetime import timedelta



#Enum class for Task_Status ========================================
class Task_Status (Enum) :
    BACKLOG = 0
    TODO  = 1
    DOING = 2
    DONE = 3
    ARCHIVED = 4


#Enum class for prioritys ========================================
class Task_priority(Enum) :
    CRITICAL = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3

#Function to making unique ID for our task using uuID library======
def make_unique_ID():
    return uuid.uuid4()



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

    def __init__(self , priority = Task_priority.LOW , title = "Task" , discription = "put your discription here" , status = Task_Status.BACKLOG ) :
        
        self.status = status
        self.discription = discription
        self.priority = priority
        self.title = title
        self.start_time = (datetime.datetime.now()).strftime("%Y-%m-%d  %H:%M:%S")
        self.end_time = (datetime.datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d  %H:%M:%S")
        self.ID  = str(make_unique_ID())
        
    def make_dict_of_tasks(self):
        if not isinstance(self.end_time , str):
            dicted_tasks = {'Title' : self.title , 'Description' : self.discription , 'Priority' : self.priority , 'Status' : self.status , "Assignees" : self.assignees ,'Comments' : self.comments , "ID" : self.ID , 'Start_time' : self.start_time.strftime("%d/%m/%Y  %H:%M:%S") ,'End_time' : self.end_time.strftime("%d/%m/%Y  %H:%M:%S") , 'History' : self.history}
        else:
            dicted_tasks = {'Title' : self.title , 'Description' : self.discription , 'Priority' : self.priority , 'Status' : self.status , "Assignees" : self.assignees ,'Comments' : self.comments , "ID" : self.ID , 'Start_time' : self.start_time ,'End_time' : self.end_time , 'History' : self.history}
        return dicted_tasks