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


#INFORMATION===========================================================
In_account_user = User(None , None , None , None , None)
in_work_project = Projects(None , None)
in_hand_task = Task(None , None , None , None)
#======================================================================

def justify_table_center(table):
    # Split the table into lines
    lines = table.split('\n')

    # Find the maximum line length
    max_length = max(len(line) for line in lines)

    # Adjust each line to center justify it
    centered_lines = [line.center(max_length) for line in lines]

    # Join the lines back together
    centered_table = '\n'.join(centered_lines)

    return centered_table

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_task_allways(in_work_project.ID , In_account_user.username)



#FUNCTION FOR SYNCING INFORMATION==================================================
def sync_information(ID , username):
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
            for project in user['projects_leads']:
                In_account_user.projects_leads.append(project)
            for project in user['projects_member']:
                In_account_user.projects_member.append(project)
    
    for project in In_account_user.projects_leads:
        if project['ID'] == ID:
            in_work_project.name = project['name']
            in_work_project.ID = project['ID']
            in_work_project.leader = project['leader']
            for member in project['members']:
                in_work_project.members_usernames.append(member)
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
#EVERYTHING STARTS HERE===========================================================
def start(IDr , usernamer):
   
    sync_information(IDr , usernamer)

    proj_path_leads = in_work_project.finding_projects_leads()
    while True:
        show_task_allways(in_work_project.ID , In_account_user.username)
        lines_list = ["1_Create a new task" , "2_Move task" , '3_Edit task' , "4_See all members" ,"5_exit "]
        Choice = pro_print_nocls(lines_list)

        if Choice == '1':
            in_work_project.create_new_task()
        elif Choice == '2':
            in_work_project.update_project()
            Move_task(in_work_project.ID , In_account_user.username)
        elif Choice == '3':
            in_work_project.update_project()
            edit_task(in_work_project.ID , In_account_user.username)
        elif Choice == '4':
            in_work_project.show_all_members(In_account_user)
        elif Choice == '5':
            break
        
#=================================================================================
#This part is for editing tasks===================================================
def edit_task(ID , username):
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

    owner_of_proj = in_work_project.finding_projects_leads()

    for task in users_info[owner_of_proj[0]][owner_of_proj[1]][owner_of_proj[2]][owner_of_proj[3]]:
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

#=================================================================================
#edit task========================================================================
def edit_it(array_2D , current_point_list):
    owner_of_proj = in_work_project.finding_projects_leads()
    Id_we_wanna_edit = ''
    try :
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

    for task in users_info[owner_of_proj[0]][owner_of_proj[1]][owner_of_proj[2]][owner_of_proj[3]]:
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
    
    Start_Editing(Id_we_wanna_edit["ID"] , In_account_user.username)

#=================================================================================

#Function for showing project info allways========================================
def show_task_allways(ID , username):
    
    table = Table(title = 'Project')
    table.add_column("BACKLOG" , justify='center' , style="blue")
    table.add_column("TODO" , justify='center' , style='green')
    table.add_column("DOING" , justify='center' , style='yellow')
    table.add_column("DONE" , justify='center' , style='purple')
    table.add_column("ARCHIVED" , justify='center' , style='red')

    owner_of_proj = in_work_project.finding_projects_leads()

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


    for task in users_info[owner_of_proj[0]][owner_of_proj[1]][owner_of_proj[2]][owner_of_proj[3]]:
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

#=================================================================================
def swap_task(origin_point , destination_point):
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

    owner_of_proj = in_work_project.finding_projects_leads()

    for task in in_work_project.tasks:
        if task.status == 'BACKLOG':
            Backlog_tasks.append(task)
        elif task.status == 'TODO':
            Todo_tasks.append(task)
        elif task.status == 'DOING':
            Doing_tasks.append(task)
        elif task.status == 'DONE':
            Done_tasks.append(task)
        elif task.status == 'ARCHIVED':
            Archived_tasks.append(task)

    all_list = [Backlog_tasks , Todo_tasks , Doing_tasks , Done_tasks , Archived_tasks]
    

    if destination_point[1] == 0:
        all_list[origin_point[1]][origin_point[0]].status = 'BACKLOG'
    elif destination_point[1] == 1:
        all_list[origin_point[1]][origin_point[0]].status = 'TODO'
    elif destination_point[1] == 2:
        all_list[origin_point[1]][origin_point[0]].status = 'DOING'
    elif destination_point[1] == 3:
        all_list[origin_point[1]][origin_point[0]].status = 'DONE'
    elif destination_point[1] == 4:
        all_list[origin_point[1]][origin_point[0]].status = 'ARCHIVED'

    extended_list = Backlog_tasks + Todo_tasks + Doing_tasks + Done_tasks + Archived_tasks
    try:
        with open('save_username_password_email.json' , 'r') as file:
            users_info = json.load(file)
            file.close()
    except : 
        users_info = []
    want_to_change_list = [In_account_user.username]

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

#Function for second part of movement=============================================
def final_move(movement_list , array_2D , text):
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
#Function for Moving task=========================================================
def Move_task(ID , username):
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
        if task.status == 'BACKLOG':
            Backlog_tasks.append(task)
        elif task.status == 'TODO':
            Todo_tasks.append(task)
        elif task.status == 'DOING':
            Doing_tasks.append(task)
        elif task.status == 'DONE':
            Done_tasks.append(task)
        elif task.status == 'ARCHIVED':
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

    array_2D = [[0, 0 , 0 , 0 , 0] for _ in range(rows)]
    
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


