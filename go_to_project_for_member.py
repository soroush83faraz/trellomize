from rich.console import Console
from rich.table import Table
import os
import json
import tasks
from printing_nocls import *
from printing import *
from tabulate import tabulate
from comment_and_member import *
from user import *
from tasks import *
from projects import *
import logging

logging.basicConfig(filename="mylog.log", level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")


def show_big_table():
        logging.info("show_big_table() called in go_to_project_for_leader.py")
        try :
            with open("save_username_password_email.json" , "r") as json_file :
                users_info = json.load(json_file)
                json_file.close()
               
        except FileNotFoundError:
            users_info = []
    
        # print(users_info[proj_path_leads[0]][proj_path_leads[1]][0][proj_path_leads[2]]) 
    
        table = Table(title="TASKS" , )
        table.add_column("Index" , justify="center" , style="bold white")
        table.add_column("Title" , justify="center" , style="cyan")
        table.add_column("Description" , justify="center" , style="green")
        table.add_column("Priority" , justify="center" , style="magenta")
        table.add_column("Status" , justify="center" , style="yellow")
        table.add_column("Comments" , justify="center" , style="blue")
        table.add_column("ID" , justify="center" , style="red")

        
        CRITICAL = []
        HIGH = []
        MEDIUM = []
        LOW = []  
        all = []  

        owner_of_proj = in_work_project.finding_projects_leads()
        for i in users_info[owner_of_proj[0]][owner_of_proj[1]][owner_of_proj[2]][owner_of_proj[3]]:
            # print(i["Title"])
            if i["Priority"] == "CRITICAL" :
                CRITICAL.append(i)
            if i["Priority"] == "HIGH" :
                HIGH.append(i)
            if i["Priority"] == "MEDIUM" :
                MEDIUM.append(i)
            if i["Priority"] == "LOW" :
                LOW.append(i)            
        if len(CRITICAL) != 0 :
            all.append(CRITICAL)
        if len(HIGH) != 0 :         
            all.append(HIGH)        
        if len(MEDIUM) !=0 :   
            all.append(MEDIUM)        
        if len(LOW) != 0 :        
            all.append(LOW)  
    
        tasks = []
        index = 0 
        for j in all : 
            for i in j :
                tasks.append(i)
                # table.add_row( str(index) , i["Title"] , i["Description"] , i["Priority"] , i["Status"] , "Comments" , i["ID"]) 
        for i in tasks :     
            index = index + 1 
            table.add_row( str(index) , i["Title"] , i["Description"] , i["Priority"] , i["Status"] , "Comments" , i["ID"]) 
        clear_terminal()     
        table = Align.center(table , vertical='bottom')   
        console = Console()
        console.print(table)  
        logging.warning(f"show big table returns {tasks}") 
        return tasks

#INFORMATION===========================================================
In_account_user = User(None , None , None , None , None)
in_work_project = Projects(None , None)
in_hand_task = Task(None , None , None , None)
#======================================================================
def justify_table_center(table):
    
    """
    Centers the content within each cell of a 2D list (table).

    Args:
        table (list): A 2D list representing the table.

    Returns:
        list: A new 2D list with centered content in each cell.
    """
    # Split the table into lines
    lines = table.split('\n')

    # Find the maximum line length
    max_length = max(len(line) for line in lines)

    # Adjust each line to center justify it
    centered_lines = [line.center(max_length) for line in lines]

    # Join the lines back together
    centered_table = '\n'.join(centered_lines)

    return centered_table

def start_for_member(IDr , username):
    logging.info(f"Arrived in start_for_member({IDr} , {username})")
    while True:
        logging.critical(f"sync_information({IDr} , {username}) called in go_to_project_for_member.py")
        sync_information(IDr , username)
        show_task_allways(in_work_project.ID , In_account_user.username)
        lines_list = [ "1_Move task" , '2_Enter task' , '3_Watch everything' , "4_exit "]
        Choice = pro_print_nocls(lines_list)

        if Choice == '1':
            logging.critical(f"in_work_project.update_project() called in go_to_project_fof_member.py")
            in_work_project.update_project()
            logging.critical(f"Move_task({in_work_project.ID} , {In_account_user.username}) called in go_to_project_for_member")
            Move_task(in_work_project.ID , In_account_user.username)
        elif Choice == '2':
            logging.critical(f"in_work_project.update_project() called in start_for_member({IDr} , {username}) in go_to_project_for_member.py")
            in_work_project.update_project()
            logging.critical(f"edit_task({in_work_project.ID} , {In_account_user.username}) is called in start_for_member({IDr} , {username} in go_to_project_for_member.py)")
            edit_task(in_work_project.ID , In_account_user.username)
        elif Choice == '3':
            logging.critical(f"inwork_project.update_project is calling in start({IDr} , {username})")
            in_work_project.update_project()
            logging.critical(f"show_big_table is calling in start({IDr} , {username})")
            show_big_table()
        elif Choice == '4':
            break


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_task_allways(in_work_project.ID , In_account_user.username)

#FUNCTION FOR SYNCING INFORMATION==================================================
def sync_information(ID , username):
    """
    Synchronizes user information and project details within the Trellomize application.

    Retrieves user data from the JSON file and updates the in-work project based on the specified project ID.

    Args:
        ID (str): The project ID.
        username (str): The username of the user.

    """
    logging.info(f"sync_information({ID} , {username}) in go_to_project_for_member.py")
    try:
        with open('save_username_password_email.json' , 'r') as file:
            users_info = json.load(file)
            file .close()
    except:
        users_info = []

    rtask = Task(None , None , None , None)
    for user in users_info:
        if user['username'] == username:
            In_account_user.username = user['username']
            In_account_user.password = user['password']
            In_account_user.email = user['email']
            In_account_user.IsActive = True
            In_account_user.projects_leads.clear()
            for project in user['projects_leads']:
                In_account_user.projects_leads.append(project)
            In_account_user.projects_member.clear()
            for project in user['projects_member']:
                In_account_user.projects_member.append(project)
    
    for project in In_account_user.projects_member:
        if project['ID'] == ID:
            in_work_project.name = project['name']
            in_work_project.ID = project['ID']
            in_work_project.leader = project['leader']
            in_work_project.members_usernames.clear()
            for member in project['members']:
                in_work_project.members_usernames.append(member)
            in_work_project.tasks.clear()
            for task in project['tasks']:
                rtask.comments = task['Comments']
                rtask.assignees = task['Assignees']
                rtask.discription = task['Description']
                rtask.end_time = task['End_time']
                rtask.history = task['History']
                rtask.ID = task['ID']
                rtask.priority = task['Priority']
                rtask.start_time = task['Start_time']
                rtask.end_time = task['End_time']
                rtask.status = task['Status']
                rtask.title = task['Title']
                in_work_project.tasks.append(rtask)

#=================================================================================
#Function for showing project info allways========================================
def show_task_allways(ID , username):
    
    """
    Displays a table of tasks organized by status columns (BACKLOG, TODO, DOING, DONE, ARCHIVED) within a project.

    Retrieves task information from the project and presents it in a tabular format.

    Args:
        ID (str): The project ID.
        username (str): The username of the user.

    """ 
    logging.info(f"show_task_allways({ID} , {username}) in go_to_project_for_member.py")
    table = Table(title = 'Project')
    table.add_column("BACKLOG" , justify='center' , style="blue")
    table.add_column("TODO" , justify='center' , style='green')
    table.add_column("DOING" , justify='center' , style='yellow')
    table.add_column("DONE" , justify='center' , style='purple')
    table.add_column("ARCHIVED" , justify='center' , style='red')

    owner_of_proj = in_work_project.finding_projects_member(username)

    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
            
            
    except FileNotFoundError:
        users_info = []

    Backlog_tasks = []
    Todo_tasks = []
    Doing_tasks = []
    Done_tasks = []
    Archived_tasks = []


    for task in owner_of_proj:
        if task['Status'] == 'BACKLOG':
            Backlog_tasks.append(task)
        elif task['Status'] == 'TODO':
            Todo_tasks.append(task)
        elif task['Status'] == 'DOING':
            Doing_tasks.append(task)
        elif task['Status'] == 'DONE':
            Done_tasks.append(task)
        elif task['Status'] == 'ARCHIVED':
            Archived_tasks.append(task)

    max_length = max([len(Backlog_tasks) , len(Todo_tasks) , len(Doing_tasks) , len(Done_tasks) , len(Archived_tasks)])

    for i in range(max_length - len(Backlog_tasks)):
        Backlog_tasks.append({'Title' : ''})
    for i in range(max_length - len(Todo_tasks)):
        Todo_tasks.append({'Title' : ''})
    for i in range(max_length - len(Doing_tasks)):
        Doing_tasks.append({'Title' : ''})
    for i in range(max_length - len(Done_tasks)):
        Done_tasks.append({'Title' : ''})
    for i in range(max_length - len(Archived_tasks)):
        Archived_tasks.append({'Title' : ''})

    
    for i in range(max_length):
        table.add_row(Backlog_tasks[i]['Title'] , Todo_tasks[i]['Title'] , Doing_tasks[i]['Title'] , Done_tasks[i]['Title'] , Archived_tasks[i]['Title'])
     
    
    console.print(table , justify='center')

def swap_task(origin_point , destination_point):
    """
    Moves a task from one status column to another within a project in the Trellomize application.

    Retrieves task information from the project and updates the task's status based on the destination column.

    Args:
        origin_point (list): A list containing the initial row and column of the task.
        destination_point (list): A list containing the target row and column for the task.

    """
    Backlog_tasks = []
    Todo_tasks = []
    Doing_tasks = []
    Done_tasks = []
    Archived_tasks = []

    # owner_of_proj = in_work_project.finding_projects_member()

    for task in in_work_project.tasks:
        if task.status == Task_Status.BACKLOG.name:
            Backlog_tasks.append(task)
        elif task.status == Task_Status.TODO.name:
            Todo_tasks.append(task)
        elif task.status == Task_Status.DOING.name:
            Doing_tasks.append(task)
        elif task.status == Task_Status.DOING.name:
            Done_tasks.append(task)
        elif task.status == Task_Status.ARCHIVED.name:
            Archived_tasks.append(task)

    all_list = [Backlog_tasks , Todo_tasks , Doing_tasks , Done_tasks , Archived_tasks]
    

    if destination_point[1] == 0:
        all_list[origin_point[1]][origin_point[0]].status = Task_Status.BACKLOG.name
    elif destination_point[1] == 1:
        all_list[origin_point[1]][origin_point[0]].status = Task_Status.TODO.name
    elif destination_point[1] == 2:
        all_list[origin_point[1]][origin_point[0]].status = Task_Status.DOING.name
    elif destination_point[1] == 3:
        all_list[origin_point[1]][origin_point[0]].status = Task_Status.DOING.name
    elif destination_point[1] == 4:
        all_list[origin_point[1]][origin_point[0]].status = Task_Status.ARCHIVED.name

    extended_list = Backlog_tasks + Todo_tasks + Doing_tasks + Done_tasks + Archived_tasks

    try:
        with open('save_username_password_email.json' , 'r') as file:
            users_info = json.load(file)
            file.close()
    except : 
        users_info = []
    want_to_change_list = [in_work_project.leader]

    for user in users_info:
        for project in user['projects_member']:
            if project['ID'] == in_work_project.ID:
                for member in project['members']:
                    want_to_change_list.append(member)


    for user in users_info:
        if user['username'] in want_to_change_list:
            for project in user['projects_leads']:
                if project['ID'] == in_work_project.ID:
                    dicted_list = []
                    for task in extended_list:
                        dicted_list.append(task.make_dict_of_tasks())
                    project['tasks'] = dicted_list
            for project in user['projects_member']:
                if project['ID'] == in_work_project.ID:
                    dicted_list = []
                    for task in extended_list:
                        dicted_list.append(task.make_dict_of_tasks())
                    project['tasks'] = dicted_list


    with open('save_username_password_email.json' , 'w') as file:
        json.dump(users_info , file , indent=4)
#=================================================================================
def final_move(movement_list , array_2D , text):
    
    """
    Allows the user to move a task within a project in the Trellomize application.

    Displays a grid of tasks organized into columns (BACKLOG, TODO, DOING, DONE, ARCHIVED).
    The user can navigate the grid and choose a task to move to a different column.
    Updates the task's status based on the user's selection.

    Args:
        movement_list (list): A list containing the initial row and column of the task.
        array_2D (list): A 2D array representing the task grid.
        text (str): Additional text (e.g., task title) associated with the movement.

    """
    logging.info(f"Arrived in final_move({movement_list} , {array_2D} , {text}) in go_to_project_or_member.py")
    origin_point_row = movement_list[0][0]
    origin_point_column = movement_list[0][1]
    
    rows = len(array_2D)
    columns = len(array_2D[0]) 

    current_row = 1
    current_column = 1
    work = True
    while True:
        if work == True:
            array_2D_saved = array_2D[current_row-1][current_column-1]
            array_2D[current_row-1][current_column-1] = array_2D[current_row-1][current_column-1] + '🥅'

        print(tabulate(array_2D , headers=['BACKLOG' , 'TODO' , 'DOING' , 'DONE' , 'ARCHIVED']))
                    
        Chosen = input('                                                                                 Choose :')
        if Chosen == 'w' and current_row > 1:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_row -= 1
            work = True
            clear_terminal()
        elif Chosen == 's' and current_row < rows:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_row += 1
            work = True
            clear_terminal()
        elif Chosen == 'a' and current_column > 1:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_column -= 1
            work = True
            clear_terminal()
        elif Chosen == 'd' and current_column < columns:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_column += 1
            work = True
            clear_terminal()
        elif Chosen == 'c':
            array_2D[current_row-1][current_column-1] = array_2D_saved
            movement_list.append([current_row , current_column])
            swap_task([origin_point_row , origin_point_column],[current_row-1 , current_column-1])
            break
        else:
            work = False
            clear_terminal()
#=================================================================================
def Move_task(ID , username):
    
    """
    Moves tasks within a project in the Trellomize application(coolest function in the code).

    Retrieves task information from user data and organizes tasks into different columns (BACKLOG, TODO, DOING, DONE, ARCHIVED).
    Allows the user to choose a task to move and updates its status.

    Args:
        ID (str): The project ID.
        username (str): The username of the user.

    """    
    logging.info(f"Arrived in Move_task({ID} , {username}) in go_to_project_for_member.py")
    # try :
    #     with open("save_username_password_email.json" , "r") as json_file :
    #         users_info = json.load(json_file)
    #         json_file.close()
            
            
    # except FileNotFoundError:
    #     users_info = []

    Backlog_tasks = []
    Todo_tasks = []
    Doing_tasks = []
    Done_tasks = []
    Archived_tasks = []

    # owner_of_proj = in_work_project.finding_projects_leads()

    for task in in_work_project.tasks:
        
        if task.status == Task_Status.BACKLOG.name:
            Backlog_tasks.append(task)
        elif task.status == Task_Status.TODO.name:
            Todo_tasks.append(task)
        elif task.status == Task_Status.DOING.name:
            Doing_tasks.append(task)
        elif task.status == Task_Status.DONE.name:
            Done_tasks.append(task)
        elif task.status == Task_Status.ARCHIVED.name:
            Archived_tasks.append(task)

    max_length = max([len(Backlog_tasks) , len(Todo_tasks) , len(Doing_tasks) , len(Done_tasks) , len(Archived_tasks)])

    for i in range(max_length - len(Backlog_tasks)):
        ftask = Task(None , None , None , None)
        ftask.title = ''
        Backlog_tasks.append(ftask)
    for i in range(max_length - len(Todo_tasks)):
        ftask = Task(None , None , None , None)
        ftask.title = ''
        Todo_tasks.append(ftask)
    for i in range(max_length - len(Doing_tasks)):
        ftask = Task(None , None , None , None)
        ftask.title = ''
        Doing_tasks.append(ftask)
    for i in range(max_length - len(Done_tasks)):
        ftask = Task(None , None , None , None)
        ftask.title = ''
        Done_tasks.append(ftask)
    for i in range(max_length - len(Archived_tasks)):
        ftask = Task(None , None , None , None)
        ftask.title = ''
        Archived_tasks.append(ftask)

    column = 5

    row = max([len(Backlog_tasks) , len(Todo_tasks) , len(Doing_tasks) , len(Done_tasks) , len(Archived_tasks)])

    show_task_allways(ID , username)

    current_row = 1
    current_column = 1

    console.print('Choose which one of tasks do you want to move 😊' , justify='center' , style='green bold')
    rows , columns = (row , column)

    array_2D = [[0 , 0 , 0 , 0 , 0] for _ in range(rows)]
    
    for num in range(len(Backlog_tasks)):
        array_2D[num][0] = Backlog_tasks[num].title
    for num in  range(len(Todo_tasks)):
        array_2D[num][1] = Todo_tasks[num].title
    for num in range(len(Doing_tasks)):
        array_2D[num][2] = Doing_tasks[num].title
    for num in range(len(Done_tasks)):
        array_2D[num][3] = Done_tasks[num].title
    for num in range(len(Archived_tasks)):
        array_2D[num][4] = Archived_tasks[num].title

    worked = True
    moving_list = []

    while True:
        if row == 0:
            console.print("There isn't any task to move" , justify='center' , style='violet bold italic')
            break
        
        elif worked == True :
            array_2D_saved = array_2D[current_row-1][current_column-1]
            array_2D[current_row-1][current_column-1] = array_2D[current_row-1][current_column-1] + '⚽'
       
        print(tabulate(array_2D , headers=['BACKLOG' , 'TODO' , 'DOING' , 'DONE' , 'ARCHIVED']))
                    
        Chosen = input('                                                                                 Choose :')
        if Chosen == 'w' and current_row > 1:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_row -= 1
            worked = True
            clear_terminal()
        elif Chosen == 's' and current_row < rows:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_row += 1
            worked = True
            clear_terminal()
        elif Chosen == 'a' and current_column > 1:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_column -= 1
            worked = True
            clear_terminal()
        elif Chosen == 'd' and current_column < columns:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_column += 1
            worked = True
            clear_terminal()
        elif Chosen == 'c' and len(array_2D[current_row-1][current_column-1]) > 1:
            moving_list.append([current_row-1 , current_column-1])
            final_move(moving_list , array_2D , array_2D_saved)
            break


        else:
            worked = False
            clear_terminal()
#=================================================================================

def edit_task(ID , username):
    
    """
    Allows the user to edit a task within a project in the Trellomize application.

    Retrieves task information based on the specified project ID and username.
    Displays a grid of tasks organized by status columns (BACKLOG, TODO, DOING, DONE, ARCHIVED).
    The user can navigate the grid and choose a task to edit.

    Args:
        ID (str): The project ID.
        username (str): The username of the user.

    """
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
            
            
    except FileNotFoundError:
        users_info = []

    Backlog_tasks = []
    Todo_tasks = []
    Doing_tasks = []
    Done_tasks = []
    Archived_tasks = []

    owner_of_proj = in_work_project.finding_projects_member(username)

    for task in owner_of_proj:
        if task['Status'] == 'BACKLOG':
            Backlog_tasks.append(task)
        elif task['Status'] == 'TODO':
            Todo_tasks.append(task)
        elif task['Status'] == 'DOING':
            Doing_tasks.append(task)
        elif task['Status'] == 'DONE':
            Done_tasks.append(task)
        elif task['Status'] == 'ARCHIVED':
            Archived_tasks.append(task)

    max_length = max([len(Backlog_tasks) , len(Todo_tasks) , len(Doing_tasks) , len(Done_tasks) , len(Archived_tasks)])
    for i in range(max_length - len(Backlog_tasks)):
        Backlog_tasks.append({'Title' : ''})
    for i in range(max_length - len(Todo_tasks)):
        Todo_tasks.append({'Title' : ''})
    for i in range(max_length - len(Doing_tasks)):
        Doing_tasks.append({'Title' : ''})
    for i in range(max_length - len(Done_tasks)):
        Done_tasks.append({'Title' : ''})
    for i in range(max_length - len(Archived_tasks)):
        Archived_tasks.append({'Title' : ''})

    column = 5
    
    row = max([len(Backlog_tasks) , len(Todo_tasks) , len(Doing_tasks) , len(Done_tasks) , len(Archived_tasks)])
    

    show_task_allways(ID , username)

    current_row = 1
    current_column = 1

    console.print('Choose which one of tasks do you want to move 😊' , justify='center' , style='green bold')
    rows , columns = (row , column)

    array_2D = [[0 , 0 , 0 , 0 , 0] for _ in range(rows)]
    
    for num in range(len(Backlog_tasks)):
        array_2D[num][0] = Backlog_tasks[num]['Title']
    for num in  range(len(Todo_tasks)):
        array_2D[num][1] = Todo_tasks[num]['Title']
    for num in range(len(Doing_tasks)):
        array_2D[num][2] = Doing_tasks[num]['Title']
    for num in range(len(Done_tasks)):
        array_2D[num][3] = Done_tasks[num]['Title']
    for num in range(len(Archived_tasks)):
        array_2D[num][4] = Archived_tasks[num]['Title']
    worked = True
    moving_list = []
    while True:
        if row == 0:
            clear_terminal()
            console.print("There isn't any task you wanna edit" , justify='center' , style='purple bold')
            break
        elif worked == True:
            array_2D_saved = array_2D[current_row-1][current_column-1]
            array_2D[current_row-1][current_column-1] = array_2D[current_row-1][current_column-1] + '✏️'
       
        print(tabulate(array_2D , headers=['BACKLOG' , 'TODO' , 'DOING' , 'DONE' , 'ARCHIVED']))
                    
        Chosen = input('                                                                                 Choose :')
        if Chosen == 'w' and current_row > 1:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_row -= 1
            worked = True
            clear_terminal()
        elif Chosen == 's' and current_row < rows:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_row += 1
            worked = True
            clear_terminal()
        elif Chosen == 'a' and current_column > 1:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_column -= 1
            worked = True
            clear_terminal()
        elif Chosen == 'd' and current_column < columns:
            array_2D[current_row-1][current_column-1] = array_2D_saved
            current_column += 1
            worked = True
            clear_terminal()
        elif Chosen == 'c' and len(array_2D[current_row-1][current_column-1]) > 2:
            moving_list.append([current_row-1 , current_column-1])
            # final_move(moving_list , array_2D , array_2D_saved)
            edit_it(array_2D , [current_row-1 , current_column-1])
            break

        else:
            worked = False
            clear_terminal()


#edit task========================================================================
def edit_it(array_2D , current_point_list):
    
    """
    Initiates the process of editing a task within the project.

    Args:
        array_2D (list): A 2D array representing the project board.
        current_point_list (list): The current position of the cursor on the board.

    Note:
        - This method identifies the task to be edited based on the cursor position.
        - It then calls the appropriate editing function (e.g., Start_editing_for_member).

    """

    
    owner_of_proj = in_work_project.finding_projects_member(In_account_user.username)
    Id_we_wanna_edit = ''
    try:
        with open('save_username_password_email.json' , 'r') as file:
            users_info = json.load(file)
            file.close()
    except FileExistsError:
        users_info = []


    Backlog_tasks = []
    Todo_tasks = []
    Doing_tasks = []
    Done_tasks = []
    Archived_tasks = []

    for task in owner_of_proj:
        if task['Status'] == 'BACKLOG':
            Backlog_tasks.append(task)
        elif task['Status'] == 'TODO':
            Todo_tasks.append(task)
        elif task['Status'] == 'DOING':
            Doing_tasks.append(task)
        elif task['Status'] == 'DONE':
            Done_tasks.append(task)
        elif task['Status'] == 'ARCHIVED':
            Archived_tasks.append(task)

    all_list = [Backlog_tasks , Todo_tasks , Doing_tasks , Done_tasks , Archived_tasks]  
    Id_we_wanna_edit = all_list[current_point_list[1]][current_point_list[0]]
    
    
    ftask = make_it_task(Id_we_wanna_edit)

    Start_editing_for_member(ftask , In_account_user , in_work_project)

#=================================================================================




            