from rich.console import Console
from rich.table import Table
import os
import json
import tasks
from printing import *


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
            users_info[proj_path_leads[0]][proj_path_leads[1]][0][proj_path_leads[2]].append(dict_of_tasks)
            with open("save_username_password_email.json"  , "w") as json_file :
                json.dump(users_info , json_file , indent=4)
                json_file.close()
            break
            
            

        else :
            print("your choice isnt valid please choose from 1 , 2 , 3 , 4 , 5")
            



def work_inside_proj (ID , username_In_Acc):
    
    proj_path_member = finding_projects_member (ID , username_In_Acc)       
    # print(proj_member) 
    proj_path_leads = finding_projects_leads (ID , username_In_Acc)     
    # print(proj_path_leads) 
    
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
               
    except FileNotFoundError:
        users_info = []
        
        
    if (proj_path_leads != None) :    
        while True :
            console.print (f"Hello dear [green][bold]{users_info[proj_path_leads[0]]["username"]}[/][/] Choose a number    ([red](*)[/] if you want to exit)" , justify='center')
            
            lines_list = ["1_Create a new task" , "2_show my tasks " , "3_Choose a task and member " , "4_ exit "]

            choice = pro_print(lines_list)
            if choice == '*' :
                break
            
            if choice == "1" :
                create_new_task(proj_path_leads)
                break
            
            if choice == "2" :
                show_task(proj_path_leads)
            
            if choice == "3" :
                task_and_member(proj_path_leads)            
            
            if choice == "4" :
                break
            
            # if choice != "1" or choice != "2" or choice != "3" or choice != "4" or choice != 3 or choice != 2 or choice != 1 :
            #     print("your choice isnt valid please choose from 1 , 2 , 3 , 4")
    else :
        console.print("You are not leading this project  ❌😊" , style='bold green' , justify='center')
            


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
                    proj_path.append("tasks")
                    #print(proj_path)
                    return proj_path

            
            
def finding_projects_member (ID , username) :
    
    
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
            
            
    except FileNotFoundError:
        users_info = []
        
    proj_path = [] 
    for user in range(len(users_info)):
        if users_info[user]['username'] == username:
            for item in range(len(users_info[user]["projects_member"])) :
                if users_info[user]["projects_member"][item]["ID"] == ID :
                    proj_path.append(user)
                    proj_path.append("projects_member")
                    proj_path.append("tasks")
                    #print(proj_path)
                    return proj_path
    


def task_and_member (proj_path_leads) :
    while True :
        clear()
        tasks = show_task (proj_path_leads) 
        ls = []
        
                
        for i in range(len(tasks)) :
            ls.append(i+1)
        while True :
            try :
                the_task = int(input("please enter the index of your task that you want to edit :"))
                break
            except :
                print (f"please enter on of these nnumbers {ls}")

        if the_task in ls :
            table = Table(title="TASKS")
            table.add_column("BACKLOG" , justify="center" , style="white")
            table.add_column("TODO" , justify="center" , style="white")
            table.add_column("DOING" , justify="center" , style="white")
            table.add_column("DONE" , justify="center" , style="white")
            table.add_column("ARCHIVED" , justify="center" , style="white")
            clear() 
            # for attributes in tasks :
            #     if attributes == tasks[the_task-1] :
            #         if attributes["Status"] == "BACKLOG" :
            #             table.add_row(attributes["Title"] , "" , "" , "" , "" , style="blue")
            #         if attributes["Status"] == "TODO" :
            #             table.add_row("" ,attributes["Title"] , "" , "" , "" , style="blue")
            #         if attributes["Status"] == "DOING" :
            #             table.add_row("" , "" , attributes["Title"] , "" , "" , style="blue")
            #         if attributes["Status"] == "HIGH" :
            #             table.add_row("" , "" , "" , attributes["Title"] , "" , style="blue")
            #         if attributes["Status"] == "ARCHIVED" :
            #             table.add_row("" , "" , "" , "" , attributes["Title"] , style="blue")                    

                  
            for attributes in tasks :
                if attributes["Status"] == "BACKLOG" :
                    if attributes != tasks[the_task-1]:                    
                        table.add_row(attributes["Title"] , "" , "" , "" , "" , style="yellow")
                    else :
                        table.add_row(attributes["Title"] , "" , "" , "" , "" , style="blue")                       
                if attributes["Status"] == "TODO" :
                    if attributes != tasks[the_task-1]:                    
                        table.add_row("" ,attributes["Title"] , "" , "" , "" , style="yellow")
                    else :
                        table.add_row("" , attributes["Title"] , "" , "" , "" , style="blue")   
                if attributes["Status"] == "DOING" :
                    if attributes != tasks[the_task-1]:                    
                        table.add_row("" , "" , attributes["Title"] , "" , "" , style="yellow")
                    else :
                        table.add_row("" , "" , attributes["Title"] , "" , "" , style="blue")   
                if attributes["Status"] == "HIGH" :
                    if attributes != tasks[the_task-1]:                    
                        table.add_row("" , "" , "" , attributes["Title"] , "" , style="yellow")
                    else :
                        table.add_row("" , "" , "" , attributes["Title"] , "" , style="blue")   
                if attributes["Status"] == "ARCHIVED" :
                    if attributes != tasks[the_task-1]:
                        table.add_row("" , "" , "" , "" , attributes["Title"] , style="yellow")
                    else :
                        table.add_row("" , "" , "" , "" , attributes["Title"] , style="blue")   
                
                    
                                    
            console = Console()
            console.print(table)  
            a = input() 
            
            
            
            
            print(tasks[the_task-1])
        else :
            print (f"please enter on of these nnumbers {ls}")

      
      
                     
            
def show_task (proj_path_leads) :
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
               
    except FileNotFoundError:
        users_info = []
    
    # print(users_info[proj_path_leads[0]][proj_path_leads[1]][0][proj_path_leads[2]]) 
    
    table = Table(title="TASKS")
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
    
    for i in users_info[proj_path_leads[0]][proj_path_leads[1]][0][proj_path_leads[2]] :
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
    clear()        
    console = Console()
    console.print(table)   
    return tasks
         
               
def clear():
    os.system('cls')            
    
# work_inside_proj("1323" , 'saeed')
