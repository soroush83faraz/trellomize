import datetime
import uuid
from enum import Enum
from history import *
from datetime import timedelta
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text


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
    history = []
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
        # for history in self.history:
        #     if isinstance(history , History):
        #         dicted = history.make_dict_of_history()
        #         self.history.remove(history)
        #         self.history.append(dicted)
        if not isinstance(self.end_time , str):
            dicted_tasks = {'Title' : self.title , 'Description' : self.discription , 'Priority' : self.priority , 'Status' : self.status , "Assignees" : self.assignees ,'Comments' : self.comments , "ID" : self.ID , 'Start_time' : self.start_time.strftime("%d/%m/%Y  %H:%M:%S") ,'End_time' : self.end_time.strftime("%d/%m/%Y  %H:%M:%S") , 'History' : self.history}
        else:
            dicted_tasks = {'Title' : self.title , 'Description' : self.discription , 'Priority' : self.priority , 'Status' : self.status , "Assignees" : self.assignees ,'Comments' : self.comments , "ID" : self.ID , 'Start_time' : self.start_time ,'End_time' : self.end_time , 'History' : self.history}
        return dicted_tasks
    

    def visit_history(self):
        console = Console()
        for text in self.history:

            custom_text = Text( f'Date :{text['Date']}'+'\n' +f'Doer :{text['Doer']}'+ '\n' + text['Content'] , style="bold magenta")
            panel = Panel(
                custom_text,
                title="History",
                title_align="center",
                border_style="bright_green",
                expand=False 
            )
            centered_panel = Align.center(panel)
            console.print(centered_panel)

    
def make_it_task(dictionary):
    ftask = Task(None , None , None , None)
    ftask.assignees = dictionary['Assignees']
    ftask.comments = dictionary['Comments']
    ftask.discription = dictionary['Description']
    ftask.end_time = dictionary['End_time']
    ftask.history = dictionary['History']
    ftask.ID = dictionary['ID']
    ftask.priority = dictionary['Priority']
    ftask.start_time = dictionary['Start_time']
    ftask.status = dictionary['Status']
    ftask.title = dictionary['Title']
    return ftask

