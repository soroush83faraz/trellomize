import json
from projects import *
from tasks import * 
from user import *
from in_project_workplace import *

new_project = Projects(None , None)
In_account_user = User(None , None , None , None , None)
pre_list_of_members = []
#Defining function for choosing name for project================
def name_project():
    print('Enter a title for your project')
    
    while True:
        title = input('Title :')
        if title == '*':
            break
        else:
            new_project.name = title
            break
            


#===============================================================
#Function for adding member to project==========================
def Add_member():
    while True:
        Added = False
        print("Enter member's name who you wanna add :")
        member_name = input('Member name :')
        if member_name == '*':
            break

        try: 
            with open('save_username_password_email.json' , 'r') as rfile:
                data = json.load(rfile)
                rfile.close()
        except:
            data = []
        
        for i in data:
            if i['username'] == member_name:
                new_project.members_usernames.append(i['username'])
                pre_list_of_members.append(i['username'])
                Added = True
                print(f"{member_name} was added to project successfully")
            
                
        if Added:
            # try:
            #     with open('save_username_password_email.json' , 'r') as rfile:
            #         existing_data = json.load(rfile)
            #         rfile.close()
            # except:
            #     existing_data = []

            # for i in existing_data:
            #     if i['username'] == member_name:
            #         i['projects_member'].append(new_project.make_dict_of_project())
            #         new_data = existing_data

            # with open('save_username_password_email.json' , 'w') as wfile:
            #     json.dump(new_data , wfile , indent=4)
            #     wfile.close()
            break
        else:
            print("The username was not found")

#===============================================================
#Functiom for saving project====================================
def save_my_project():
    proj_ID = []
    if new_project.name == None:
        print("You should pick a title for your project")
    elif new_project.ID == None:
        print("You should pick an ID for your project")
    
    try:
        with open('save_username_password_email.json' , 'r') as file: 
            users = json.load(file)
            file.close()
    except:
        users = []

    for user in users:
        for project_lead in user['projects_leads']:
            proj_ID.append(project_lead['ID'])
        for project_member in user['projects_member']:
            proj_ID.append(project_member['ID'])

    if new_project.ID in proj_ID:
        return

    else:
        members_name = []
        for username in new_project.members_usernames:
            members_name.append(username)

        new_project.leader = In_account_user.username
        
        # with open("Projects.json" , 'w') as wfile:
        #     project_dict = {'title' : new_project.name , "members" : members_name, "ID" : new_project.ID , "leader" : new_project.leader , "tasks" : new_project.tasks}
        #     json.dump(project_dict , wfile , indent=4)
        #     wfile.close()
        
        In_account_user.projects_leads.append(new_project.make_dict_of_project())

        try:
            with open('save_username_password_email.json' , 'r') as rfile:
                existing_data = json.load(rfile)
                rfile.close()
        except:
            existing_data = []

        for user in existing_data:
            if user['username'] == In_account_user.username:
                user['projects_leads'] = In_account_user.projects_leads
                
            with open('save_username_password_email.json' , 'w') as wfile:
                json.dump(existing_data , wfile , indent=4)
                wfile.close()
    #Section for saving project info into usernames dictionary==
        try:
            with open('save_username_password_email.json' , 'r') as file:
                user_info = json.load(file)
                file.close()
        except:
            user_info = []

        for user in user_info:
            if user['username'] in members_name:
                user['projects_member'].append(new_project.make_dict_of_project())

        with open('save_username_password_email.json' , 'w') as wfile:
            json.dump(user_info , wfile , indent=4)
            wfile.close()
    #===========================================================
                


#===============================================================
#Function for getting ID for project an validate it=============
def get_ID():
    print("You should enter an unique ID for your project")
    while True:
        ID = input("ID :")

        if ID == '*':
            break
        try:
            with open('save_username_password_email.json' , 'r') as file:
                all_users_data = json.load(file)
                file.close()
        except:
            all_users_data = []

        list_of_project_ID = []
        for user in all_users_data:
            if user['username'] == In_account_user.username:
                for project in user['projects_leads']:
                    list_of_project_ID.append(project['ID'])
                for project in user['projects_member']:
                    list_of_project_ID.append(project['ID'])





        if ID in list_of_project_ID:
            print("Choose an unique ID")
        else:
            new_project.ID = ID
            print('ID set')
            break




#===============================================================
#Fuction for showing projects===================================
def show_all_projects():
    try:
        with open('save_username_password_email.json' , 'r') as file:
            users_info = json.load(file)
            file.close()
    except:
        users_info = []
    counter = 1

    proj_list = []
    for user in users_info:
        if user['username'] == In_account_user.username:
            for project in user['projects_leads']:
                print(f"{counter}_{project['name']}    (leader)")
                proj_list.append(project)
                counter += 1
            for proj in user["projects_member"]:
                print(f"{counter}_{proj['name']}       (member)")
                proj_list.append[proj]
                counter += 1
        
    print('Wanna work on your project?')
    print('1_Yes')
    print("2_NO")
    chosen_option = input('Choose :')
    
    if chosen_option == '1':
        while True:
            print('Which project?')
            proj_number = input("project number :") 
            if proj_number > 0 and proj_number < counter:
                       work_inside_proj(proj_list[proj_number]['ID'])

        
#===============================================================

#Function for making new project in mainpage of App=============
def Creat_new_project():
    
    while True:
        member_list = []
        for i in new_project.members_usernames:
            member_list.append(i)
        print(f"Dear {In_account_user.username} Fill it to make project")
        print(f"1_Project's title:{new_project.name}")
        print(f"2_Project's members {member_list}")
        print(f"3_Project's ID :{new_project.ID}")
        print("4_Save")
        print("5_exit")

        chosen_option = input('Choose :')

        if chosen_option == '1':
            name_project()

        elif chosen_option == '2':
            Add_member()
        elif chosen_option == '3':
            get_ID()
        elif chosen_option == '4':
            save_my_project()
        elif chosen_option == '5':
            break

#===============================================================

def Work_inside_Trellomize(datalist):
    In_account_user.username = datalist['username']
    In_account_user.password = datalist['password']
    In_account_user.email = datalist['email']
    In_account_user.projects_leads = datalist['projects_leads']
    In_account_user.projects_member = datalist['projects_member']

    while True:
        print(f'Dear {In_account_user.username} Choose a number & (*) to exit')
        print('1_Creat new project')
        print("2_View all projects")

        chosen_option = input("Choose your option")

        if chosen_option == '*':
            break
        
        elif chosen_option == '1':
            Creat_new_project()

        elif chosen_option == '2':
            show_all_projects()