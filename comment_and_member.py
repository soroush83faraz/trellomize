import json
from printing import* 
from comment import *
from datetime import datetime
from projects import Projects
from tasks import Task ,  make_it_task
from user import *
from history import *
# from projects import *
# from tasks import * 
# from user import *
# from in_project_workplace import *
# from printing import *
# from saeed_mode_on import *

inhand_comment = Commento(None)
in_hand_project = Projects(None , None)


def Comment(gtask , InAccUser , gproj):
    comment = input("please enter your comment here : ")
    
    inhand_comment.writer = InAccUser.username 
    inhand_comment.text = comment
    inhand_comment.time = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    

    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
               
    except FileNotFoundError:
        users_info = []
    
    for user in range(len(users_info)) :
        for proj in range(len(users_info[user]["projects_leads"])) :
            for tasks in users_info[user]["projects_leads"][proj]["tasks"] :
                if gtask.ID == tasks["ID"] :
                    tasks["Comments"].append(inhand_comment.converting_to_dictionary())
                    fhistory = History() 
                    fhistory.doer = InAccUser.username
                    fhistory.content = f"{InAccUser.username} wrote a comment for {gtask.title}"  
                    fhistory.date = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
                    tasks['History'].append(fhistory.make_dict_of_history())
    for user in range(len(users_info)) :
        for proj in range(len(users_info[user]["projects_member"])) :
            for tasks in users_info[user]["projects_member"][proj]["tasks"] :
                if gtask.ID == tasks["ID"] :
                    tasks["Comments"].append(inhand_comment.converting_to_dictionary())
                    fhistory = History() 
                    fhistory.doer = InAccUser.username
                    fhistory.content = f"{InAccUser.username} wrote a comment for {gtask.title}"  
                    fhistory.date = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
                    tasks['History'].append(fhistory.make_dict_of_history()) 
                     
    with open("save_username_password_email.json"  , "w") as json_file :
        json.dump(users_info , json_file , indent=4)
        json_file.close()                   
                    
def assigning_task_to_member (gtask , InAccUser , gproj) :
    in_hand_project.ID = gproj.ID
    in_hand_project.update_project()
    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
               
    except FileNotFoundError:
        users_info = []
    
    main_task = []
    
    for user in range(len(users_info)) :
        for proj in range(len(users_info[user]["projects_leads"])) :
            for task in users_info[user]["projects_leads"][proj]["tasks"] :
                if gtask.ID == task["ID"] :
                    main_task = task
                    
                    print ("choose a member ")
                    members = users_info[user]["projects_leads"][proj]["members"]
                    for i in range(len(members)) :
                        print(f"-{i+1} {members[i]}")
                    while True :    
                        try :
                            choosen_numer = int(input())
                            if choosen_numer <= len(members) and choosen_numer > 0 :
                                break
                            else :
                                print(f"please enter a number from 1 to {len(members)}")
                        except :
                            print("please enter a number")


                    for task in in_hand_project.tasks:
                        if task.ID == gtask.ID and members[choosen_numer - 1] not in task.assignees:
                            task.assignees.append(members[choosen_numer - 1])

                    fhistory = History()
                    fhistory.content = f"{InAccUser.username} assign {members[choosen_numer - 1]} to the task"
                    fhistory.doer = InAccUser.username
                    fhistory.date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                    task.history.append(fhistory.make_dict_of_history())
                    in_hand_project.save_into_json()
                    break

                    
def remove_assignees(gtask , inAccUser , gproj):
    in_hand_project.ID = gproj.ID
    in_hand_project.update_project()
    console.print('Wich assignee do you want to remove?' , justify='center' , style='green')
    assignees_list = []
    for assignee in gtask.assignees:
        assignees_list.append(assignee)

    chosen = int(pro_print(assignees_list))

    for task in in_hand_project.tasks:
        if task.ID == gtask.ID:
            task.assignees.pop(chosen-1)
            
    in_hand_project.save_into_json()



def change_priority(gtask , InAccUser , gproj):
    in_hand_project.ID = gproj.ID
    in_hand_project.update_project()
    console.print(f'Here is the priority{gtask.status}' , justify='center' , style='bold')
    priority_list = ['CRITICAL' , 'HIGH' , 'MEDIUM' , 'LOW']

    chosen = pro_print(priority_list)

    if chosen == '1':
        for task in in_hand_project.tasks:
            if task.ID == gtask.ID:
                task.priority = "CRITICAL"
                fhistory = History() 
                fhistory.doer = InAccUser.username
                fhistory.content = f"{InAccUser.username} changed  {gtask.title}'s priority"  
                fhistory.date = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
                task.history.append(fhistory.make_dict_of_history())
    elif chosen == '2':
        for task in in_hand_project.tasks:
            if task.ID == gtask.ID:
                task.priority = "HIGH"
                fhistory = History() 
                fhistory.doer = InAccUser.username
                fhistory.content = f"{InAccUser.username} changed  {gtask.title}'s priority"  
                fhistory.date = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
                task.history.append(fhistory.make_dict_of_history())
    elif chosen == '3':
        for task in in_hand_project.tasks:
            if task.ID == gtask.ID:
                task.priority = "MEDIUM"
                fhistory = History() 
                fhistory.doer = InAccUser.username
                fhistory.content = f"{InAccUser.username} changed  {gtask.title}'s priority"  
                fhistory.date = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
                task.history.append(fhistory.make_dict_of_history())
    elif chosen == '4':
        for task in in_hand_project.tasks:
            if task.ID == gtask.ID:
                task.priority = "LOW"
                fhistory = History() 
                fhistory.doer = InAccUser.username
                fhistory.content = f"{InAccUser.username} changed  {gtask.title}'s priority"  
                fhistory.date = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
                task.history.append(fhistory.make_dict_of_history())

    

    in_hand_project.save_into_json()



def Start_Editing(gtask , InAccUser , gproj):
    
    lines_list = ['1_Add_comment_to_this_task' , '2_Assign a member to this task' , '3_Remove assignee' , '4_Change priority of tasks' , '5_Watch history of the task' , '6_Watch all comments']
    Chosen = pro_print(lines_list)

    if Chosen == '1':
        Comment(gtask , InAccUser , gproj)
    elif Chosen == '2':
        assigning_task_to_member(gtask , InAccUser , gproj)
    elif Chosen == '3':
        remove_assignees(gtask , InAccUser , gproj)
    elif Chosen == '4':
        change_priority(gtask , InAccUser , gproj)
    elif Chosen == '5':
        gtask.visit_history()
    elif Chosen == '6' : 
        gtask.watch_comments()
    
        

def Start_editing_for_member(gtask , InAccUser , gproj):
    lines_list = ['1_Add_comment_to_this_task' , '2_Change priority of tasks' , '3_Watch history of the task' ]
    Chosen = pro_print(lines_list)

    if Chosen == '1':
        Comment(gtask , InAccUser , gproj)
    elif Chosen == '2':
        change_priority(gtask , InAccUser , gproj)
    elif Chosen == '3':
        gtask.visit_history()
    elif Chosen == '4':
        gtask.watch_comments()
    
