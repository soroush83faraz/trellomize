from rich.console import Console
from rich.table import Table
import json
import tasks




def create_new_task (proj_path_leads) :
    
    Title = "Task"
    Description = "Put your discription here"
    Priority = "LOW"
    status = "BACKLOG"
    while True :
        
        print("Choose a number & (*) to exit")
        print(f"1-Title : {Title}")
        print(f"2-Description : {Description}")
        print(f"3-Priority : {Priority}")
        print(f"4-status :{status}")
        print(f"5-save Task")
        choice = input("Choose an option :")
        
        if choice == '*' :
            break
        
        elif choice == "1" :
            Title = input("Title : ")
            
        elif choice == "2" :
            Description = input("Description : ")
            
        elif choice == "3" :
            Priority = input("Priority : ")
            if Priority != "CRITICAL" and Priority != "HIGH" and Priority != "MEDIUM" and Priority != "LOW" :
                print("You should choose a priority from (CRITICAL , HIGH , MEDIUM , LOW)")
                Priority = None
                
        if choice == "4" :
            status = input("status :")
            if status != "BACKLOG" and status != "TODO" and status != "DOING" and status != "DONE" and status != "ARCHIVED" :
                print("You should choose a status from (BACKLOG , TODO , DOING , DONE , ARCHIVED)")
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
            
            

        else :
            print("your choice isnt valid please choose from 1 , 2 , 3 , 4 , 5")
            



def work_inside_proj (ID) :
    
    proj_path_member = finding_projects_member (ID)       
    # print(proj_member) 
    proj_path_leads = finding_projects_leads (ID)     
    # print(proj_path_leads) 
    
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
               
    except FileNotFoundError:
        users_info = []
        
        
    if (proj_path_leads != None) :    
        while True :
            print (f"hello dear {users_info[proj_path_leads[0]]["username"]} Choose a number    ((*) if you want to exit)")
            print("1_Create a new task")
            print("2_show my tasks ")
            print("3_Choose a task and member ")
            print("4_ exit ")
            print("Choose your option : ")
            choice = input()
            if choice == '*' :
                break
            
            if choice == "1" :
                create_new_task(proj_path_leads)
                break
            
            if choice == "2" :
                show_task(proj_path_leads)
            
            if choice == "3" :
                pass
            
            if choice == "4" :
                break
            
            if choice != "1" or choice != "2" or choice != "3" or choice != "4" :
                print("your choice isnt valid please choose from 1 , 2 , 3 , 4")
    else :
        print("you are not leading in this project ")
            


def finding_projects_leads (ID) :
    
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
            
            
    except FileNotFoundError:
        users_info = []
        
    proj_path = [] 
    for user in range(len(users_info)) :
        for item in range(len(users_info[user]["projects_leads"])) :
            if users_info[user]["projects_leads"][item]["ID"] == ID :
                proj_path.append(user)
                proj_path.append("projects_leads")
                proj_path.append("tasks")
                #print(proj_path)
                return proj_path
            
            
def finding_projects_member (ID) :
    
    
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
            
            
    except FileNotFoundError:
        users_info = []
        
    proj_path = [] 
    for user in range(len(users_info)) :
        for item in range(len(users_info[user]["projects_member"])) :
            if users_info[user]["projects_member"][item]["ID"] == ID :
                proj_path.append(user)
                proj_path.append("projects_member")
                proj_path.append("tasks")
                #print(proj_path)
                return proj_path
    
def task_and_member () :
    pass              
            
            
def show_task (proj_path_leads) :
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
               
    except FileNotFoundError:
        users_info = []
    
    # print(users_info[proj_path_leads[0]][proj_path_leads[1]][0][proj_path_leads[2]]) 
    
    table = Table(title="TASKS")
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
    # print(all)
     
    for j in all : 
        for i in j :
                   
            table.add_row(i["Title"] , i["Description"] , i["Priority"] , i["Status"] , "Comments" , i["ID"]) 
        
    console = Console()
    console.print(table)    
         
            
    
work_inside_proj("1323")
