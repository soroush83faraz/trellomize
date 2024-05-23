from rich.console import Console
from rich.table import Table
import os
import json
import tasks
from printing_nocls import *
from printing import *
from tabulate import tabulate


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

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    show_task_allways(ID , username)
#EVERYTHING STARTS HERE===========================================================
def start(IDr , usernamer):
    global ID
    ID = IDr
    global username
    username = usernamer

    proj_path_leads = finding_projects_leads(ID , username)
    while True:
        show_task_allways(ID , username)
        lines_list = ["1_Create a new task" , "2_Move task" , '3_Edit task' , "4_exit "]
        Choice = pro_print_nocls(lines_list)

        if Choice == '1':
            create_new_task(proj_path_leads)
        elif Choice == '2':
            Move_task(ID , username)
        elif Choice == '3':
            edit_task(ID , username)
        elif Choice == '4':
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

    owner_of_proj = finding_projects_leads(ID , username)

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

    array_2D = [[0, 0 , 0 , 0 , 0] for _ in range(rows)]
    
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
        if worked == True:
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
        elif Chosen == 'c' and len(array_2D[current_row-1][current_column-1]) > 1:
            moving_list.append([current_row-1 , current_column-1])
            # final_move(moving_list , array_2D , array_2D_saved)
            edit_task(array_2D , [current_row-1 , current_column-1])
            break

        else:
            worked = False
            clear_terminal()

#=================================================================================
#edit task========================================================================
def edit_task(array_2D , current_point_list):
    owner_of_proj = finding_projects_leads(ID , username)
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
    
      
    

#=================================================================================

#Function for finding user info by ID ============================================
def finding_projects_leads (ID , username) :
    
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
            
            
    except FileNotFoundError:
        users_info = []
        
    proj_path = [] 
    for user in range(len(users_info)) :
        if users_info[user]['username'] == username:
            for item in range(len(users_info[user]["projects_leads"])) :
                if users_info[user]["projects_leads"][item]["ID"] == ID :
                    proj_path.append(user)
                    proj_path.append("projects_leads")
                    proj_path.append(item)
                    proj_path.append("tasks")
                    #print(proj_path)
                    return proj_path
                
#=================================================================================
#Function for creating new task===================================================
def create_new_task (proj_path_leads) :
    

    Title = "Task"
    Description = "Put your discription here"
    Priority = "LOW"
    status = "BACKLOG"
    while True :
        
        console.print("[violet]Choose a number &[/] [red](*)[/] [violet]to exit[/]" , justify='center')
        lines_list = [f"1-Title : {Title}" , f"2-Description : {Description}" , f"3-Priority : {Priority}" , f"4-status :{status}" , f"5-save Task" , '6_Exit']
        choice = pro_print(lines_list)
        
        if choice == '6' :
            break
        
        elif choice == "1" :
            Title = input("                                                                                 Title : ")
            
        elif choice == "2" :
            Description = input("                                                                                 Description : ")
            
        elif choice == "3" :
            Priority = input("                                                                                 Priority : ")
            if Priority != "CRITICAL" and Priority != "HIGH" and Priority != "MEDIUM" and Priority != "LOW" :
                console.print("[violet][bold]You should choose a priority from [/][/][red][italic](CRITICAL , HIGH , MEDIUM , LOW)[/][/]  😊" , justify='center')
                Priority = None
                
        if choice == "4" :
            status = input("status :")
            if status != "BACKLOG" and status != "TODO" and status != "DOING" and status != "DONE" and status != "ARCHIVED" :
                console.print("[violet][bold]You should choose a status from[/][/][red][italic] (BACKLOG , TODO , DOING , DONE , ARCHIVED) [/][/]" , justify='center')
                status = None
                
        elif choice == "5" :
            task = tasks.Task(Priority , Title , Description , status)
            dict_of_tasks = task.make_dict_of_tasks()
            # print(dict_of_tasks)
            try :
                with open("save_username_password_email.json" , "r") as json_file :
                    users_info = json.load(json_file)
                    json_file.close()


            except FileNotFoundError:
                users_info = []
            # print(users_info[proj_path_leads[0]][proj_path_leads[1]][0])
            users_info[proj_path_leads[0]][proj_path_leads[1]][proj_path_leads[2]][proj_path_leads[3]].append(dict_of_tasks)
            with open("save_username_password_email.json"  , "w") as json_file :
                json.dump(users_info , json_file , indent=4)
                json_file.close()
            break
            
            

        else :
            print("your choice isnt valid please choose from 1 , 2 , 3 , 4 , 5")
            


#=================================================================================
#Function for showing project info allways========================================
def show_task_allways(ID , username):
    
    table = Table(title='Project')
    table.add_column("BACKLOG" , justify='center' , style="blue")
    table.add_column("TODO" , justify='center' , style='green')
    table.add_column("DOING" , justify='center' , style='yellow')
    table.add_column("DONE" , justify='center' , style='purple')
    table.add_column("ARCHIVED" , justify='center' , style='red')
    
    

    owner_of_proj = finding_projects_leads(ID , username)

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

    owner_of_proj = finding_projects_leads(ID , username)

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
    

    if destination_point[1] == 0:
        all_list[origin_point[1]][origin_point[0]]['Status'] = 'BACKLOG'
    elif destination_point[1] == 1:
        all_list[origin_point[1]][origin_point[0]]['Status'] = 'TODO'
    elif destination_point[1] == 2:
        all_list[origin_point[1]][origin_point[0]]['Status'] = 'DOING'
    elif destination_point[1] == 3:
        all_list[origin_point[1]][origin_point[0]]['Status'] = 'DONE'
    elif destination_point[1] == 4:
        all_list[origin_point[1]][origin_point[0]]['Status'] = 'ARCHIVED'

    extended_list = Backlog_tasks + Todo_tasks + Doing_tasks + Done_tasks + Archived_tasks
    try:
        with open('save_username_password_email.json' , 'r') as file:
            users_info = json.load(file)
            file.close()
    except : 
        users_info = []

    for user in users_info:
        if user['username'] == username:
            for project in user['projects_leads']:
                if project['ID'] == ID:
                    project['tasks'] = extended_list

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

    owner_of_proj = finding_projects_leads(ID , username)

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

    array_2D = [[0, 0 , 0 , 0 , 0] for _ in range(rows)]
    
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
        if worked == True:
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





