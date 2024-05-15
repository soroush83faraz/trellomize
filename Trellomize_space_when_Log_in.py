import json
from projects import *
from tasks import * 
from user import *
new_project = Projects(None , None)
In_account_user = User(None , None , None , None , None)
pre_list_of_members = []
#Defining function for choosing name for project================
def name_project():
    print('Enter a name for your project')
    
    while True:
        

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
    proj_names = []
    if new_project.name == None:
        print("You should pick a title for your project")
    
    try:
        with open('Projects.json' , 'r') as file: 
            projs = json.load(file)
            file.close()
    except:
        projs = []

    for i in projs:
        proj_names.append(i['title'])
    if new_project.name in proj_names:
        return

    else:
        members_name = []
        for i in new_project.members_usernames:
            members_name.append(i)

        new_project.leader = In_account_user.username
        
        with open("Projects.json" , 'w') as wfile:
            project_dict = {'title' : new_project.name , "members" : members_name, "ID" : new_project.ID , "leader" : new_project.leader , "tasks" : new_project.tasks}
            json.dump(project_dict , wfile , indent=4)
            wfile.close()
        
        In_account_user.projects_leads.append(new_project.make_dict_of_project())

        try:
            with open('save_username_password_email.json' , 'r') as rfile:
                existing_data = json.load(rfile)
                rfile.close()
        except:
            existing_data = []

        for i in existing_data:
            if i['username'] == In_account_user.username:
                i['projects_leads'] = In_account_user.projects_leads
                new_data = existing_data
            with open('save_username_password_email.json' , 'w') as wfile:
                json.dump(new_data , wfile , indent=4)
                wfile.close()
    #Section for saving project info into usernames dictionary==
        try:
            with open('save_username_password_email.json' , 'r') as file:
                user_info = json.load(file)
                file.close()
        except:
            user_info = []

        for i in user_info:
            if i['username'] in members_name:
                i['projects_member'].append(new_project.make_dict_of_project())

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
                for project in user['project']:
                    list_of_project_ID.append(project['ID'])




        if ID in list_of_project_ID:
            print("Choose an unique ID")
        else:
            new_project.ID = ID
            print('ID set')
            break




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
        print('3_View projects you lead')
        print("4_View projects you're asignees")

        chosen_option = input("Choose your option")

        if chosen_option == '*':
            break
        
        elif chosen_option == '1':
            Creat_new_project()

        elif chosen_option == '2':
            All_user_projects = []
            try:
                with open('save_username_password_email.json' , 'r') as file:
                    users_info = json.load(file)
                    file.close()
            except:
                users_info = []

            for i in users_info:
                


