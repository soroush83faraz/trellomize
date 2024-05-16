import rich
import json
import tasks




def create_new_task (proj_leads) :
    
    Title = None
    Description = None
    Priority = None
    status = None
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
            # print(task.end_time)
            break
            

        else :
            print("your choice isnt valid please choose from 1 , 2 , 3 , 4 , 5")
            



def work_inside_proj (ID) :
    
    proj_member = finding_projects_member (ID)       
    print(proj_member) 
    proj_leads = finding_projects_leads (ID)       
    print(proj_leads) 
    while True :
        print (f"hello dear {proj_leads[0]["leader"]} Choose a number & (*) to exit")
        print("1_Create a new task")
        print("2_Choose a task and member ")
        print("3_ exit ")
        print("Choose your option : ")
        choice = input()
        if choice == '*' :
            break
        if choice == "1" :
            create_new_task(proj_leads)
            break
        if choice == "2" :
            pass 
        if choice == "3" :
            break
        else :
            print("your choice isnt valid please choose from 1 , 2 , 3 ")
            


def finding_projects_leads (ID) :
    
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
            
            
    except FileNotFoundError:
        users_info = []
        
        
    for user in users_info :
        for item in user["projects_leads"] :
            if item["ID"] == ID :
                return user["projects_leads"]
            
            
def finding_projects_member (ID) :
    
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
            
            
    except FileNotFoundError:
        users_info = []
        
            
    for user in users_info :
        for item in user["projects_member"] :
            if item["ID"] == ID :
                return user["projects_member"]
            

    
                
            
            
            
            
    
work_inside_proj("1323")
