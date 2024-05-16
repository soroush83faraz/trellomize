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
        self.ID  = make_unique_ID()
        
