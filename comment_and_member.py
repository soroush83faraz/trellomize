import json
# from projects import *
# from tasks import * 
# from user import *
# from in_project_workplace import *
# from printing import *
# from saeed_mode_on import *
def Comment(ID) :
   
    comment = input("please enter your comment here : ") 

    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
               
    except FileNotFoundError:
        users_info = []
    
    for user in range(len(users_info)) :
        for proj in range(len(users_info[user]["projects_leads"])) :
            for tasks in users_info[user]["projects_leads"][proj]["tasks"] :
                if ID == tasks["ID"] :
                    tasks["Comments"].append(comment)    
    for user in range(len(users_info)) :
        for proj in range(len(users_info[user]["projects_member"])) :
            for tasks in users_info[user]["projects_member"][proj]["tasks"] :
                if ID == tasks["ID"] :
                    tasks["Comments"].append(comment) 
                     
    with open("save_username_password_email.json"  , "w") as json_file :
        json.dump(users_info , json_file , indent=4)
        json_file.close()                   
                    
                      

def assigning_task_to_member (ID) :


    try :
        with open("save_username_password_email.json" , "r") as json_file :
            users_info = json.load(json_file)
            json_file.close()
               
    except FileNotFoundError:
        users_info = []
    
    main_task = []
    
    for user in range(len(users_info)) :
        for proj in range(len(users_info[user]["projects_leads"])) :
            for tasks in users_info[user]["projects_leads"][proj]["tasks"] :
                if ID == tasks["ID"] :
                    main_task = tasks
                    
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

                    
                    for name in range(len(users_info)) :
                        if users_info[name]["username"] == members[choosen_numer-1] :    
                            for projects in range(len(users_info[name]["projects_member"])) :
                                if users_info[name]["projects_member"][projects]["ID"] == users_info[user]["projects_leads"][proj]["ID"] :
                                    
                                    checking_task = True
                                    for alltasks in users_info[name]["projects_member"][projects]["tasks"] :
                                        if alltasks == main_task :
                                            checking_task = False
                                            # print("false")
                                            
                                    if checking_task :    
                                        users_info[name]["projects_member"][projects]["tasks"].append(main_task)
                                    with open("save_username_password_email.json"  , "w") as json_file :
                                        json.dump(users_info , json_file , indent=4)
                                        json_file.close()
                                    # print(users_info[name]["projects_member"][projects]["tasks"])
                                    
                                    
                                    
                    
                    # print(users_info[user]["projects_leads"][proj]["ID"])
                    break
                    




 


Comment("2f951f25-a4b4-4d72-8fc1-d2e2eb932c6f")



