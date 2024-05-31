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
    
    """
    Task class representing a task.
    Attributes:
        ID (str): The task's ID.
        title (str): The task's main title.
        discription (str): The task's discription that you want to add.
        start_time (str): The task's time of start .
        end_time (str): The task's time of end that you give (default : 24 hours later).
        assignees (list): The task's assignments.   
        status (str): The task's status (BACKLOG , TODO , DOING , DONE , ARCHIVED) 

    """
       
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
        
        """
        Initializes a new task.

        Args:
            priority (str): The priority level of the task (e.g., 'LOW', 'MEDIUM', 'HIGH').
            title (str): The title of the task.
            description (str): The description of the task.
            status (str): The status of the task (e.g., 'BACKLOG', 'TODO', 'DOING', 'DONE', 'ARCHIVED').

        Attributes:
            status (str): The status of the task.
            description (str): The description of the task.
            priority (str): The priority level of the task.
            title (str): The title of the task.
            start_time (str): The start time of the task (formatted as '%Y-%m-%d %H:%M:%S').
            end_time (str): The end time of the task (formatted as '%Y-%m-%d %H:%M:%S').
            ID (str): The unique identifier for the task.
        """
        
        self.status = status
        self.discription = discription
        self.priority = priority
        self.title = title
        self.start_time = (datetime.datetime.now()).strftime("%Y-%m-%d  %H:%M:%S")
        self.end_time = (datetime.datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d  %H:%M:%S")
        self.ID  = str(make_unique_ID())
        
    def make_dict_of_tasks(self):
        
        """
        Creates a dictionary representation of the task.
    
        Returns:
            dict: A dictionary containing task information.
        """


        if not isinstance(self.end_time , str):
            dicted_tasks = {'Title' : self.title , 'Description' : self.discription , 'Priority' : self.priority , 'Status' : self.status , "Assignees" : self.assignees ,'Comments' : self.comments , "ID" : self.ID , 'Start_time' : self.start_time.strftime("%d/%m/%Y  %H:%M:%S") ,'End_time' : self.end_time.strftime("%d/%m/%Y  %H:%M:%S") , 'History' : self.history}
        else:
            dicted_tasks = {'Title' : self.title , 'Description' : self.discription , 'Priority' : self.priority , 'Status' : self.status , "Assignees" : self.assignees ,'Comments' : self.comments , "ID" : self.ID , 'Start_time' : self.start_time ,'End_time' : self.end_time , 'History' : self.history}
        return dicted_tasks
    
    def watch_comments(self):
        console = Console()
        for text in self.comments:

            custom_text = Text( f'Time :{text['Time']}'+'\n' +f'Writer :{text['Writer']}'+ '\n' + text['Text'] , style="bold magenta")
            panel = Panel(
                custom_text,
                title="Comment",
                title_align="center",
                border_style="bright_green",
                expand=False 
            )
            centered_panel = Align.center(panel)
            console.print(centered_panel)

    def visit_history(self):
        
        """
        Displays the task's history.

        Note:
            This method prints the history information for the task.

        """
        
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
    
    """
    Creates a Task instance from a dictionary representation.

    Args:
        dictionary (dict): A dictionary containing task information.

    Returns:
        Task: An instance of the Task class.
    """
    
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

