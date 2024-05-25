import json
from printing import* 
from comment import *
from datetime import datetime
from projects import Projects
from tasks import Task ,  make_it_task
from user import *
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
    for user in range(len(users_info)) :
        for proj in range(len(users_info[user]["projects_member"])) :
            for tasks in users_info[user]["projects_member"][proj]["tasks"] :
                if gtask.ID == tasks["ID"] :
                    tasks["Comments"].append(inhand_comment.converting_to_dictionary()) 
                     
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
                        if task.ID == gtask.ID:
                            task.assignees.append(members[choosen_numer - 1])

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

def Start_Editing(gtask , InAccUser , gproj):
    
    lines_list = ['1_Add_comment_to_this_task' , '2_Assign a member to this task' , '3_Remove assignee']
    Chosen = pro_print(lines_list)

    if Chosen == '1':
        Comment(gtask , InAccUser , gproj)
    elif Chosen == '2':
        assigning_task_to_member(gtask , InAccUser , gproj)
    elif Chosen == '3':
        remove_assignees(gtask , InAccUser , gproj)


