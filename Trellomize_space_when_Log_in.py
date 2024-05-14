import json
from projects import *
from tasks import * 
new_project = Projects(None , None)
#Defining function for choosing name for project================
def name_project():
    while True:
        duplicate = False
        print("Choose name for project : (*) for exit")
        
        name = input("Name :")

        if name == '*':
            break

        try:
            with open('Projects.json' , 'r') as rfile:
                data = json.read(rfile)
                rfile.close()
        except:
            data = []

            for i in data:
                if name == i['name']:
                    print("Duplicate projectname! Try again")
                    duplicate = True
        
        if not duplicate:
            new_project.name = name
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
                new_project.members.append(i)
                Added = True
                print(f"{member_name} was added to project successfully")
                
        if Added:
            try:
                with open('save_username_password_email.json' , 'r') as rfile:
                    existing_data = json.load(rfile)
                    rfile.close()
            except:
                existing_data = []

            for i in existing_data:
                if i['username'] == member_name:
                    i['projects'].append(new_project.name)
                    new_data = existing_data

            with open('save_username_password_email.json' , 'w') as wfile:
                json.dump(new_data , wfile , indent=4)
                wfile.close()
            break
        else:
            print("The username was not found")

#===============================================================
#Functiom for saving project====================================
def save_my_project(datalist):
    if new_project.name == None:
        print("You should pick a title for your project")
    else:
        for i in new_project.members:
            members_name = i['username']

        new_project.leader = datalist['username']
        
        with open("Projects.json" , 'w') as wfile:
            project_dict = {'title' : new_project.name , "members" : members_name, "ID" : new_project.ID , "leader" : new_project.leader , "tasks" : new_project.tasks}
            json.dump(project_dict , wfile , indent=4)
            wfile.close()
        
        datalist['projects'].append(new_project.name)

        try:
            with open('save_username_password_email.json' , 'r') as rfile:
                existing_data = json.load(rfile)
                rfile.close()
        except:
            existing_data = []

        for i in existing_data:
            if i['username'] == datalist['username']:
                i['projects'] = datalist['projects']
                new_data = existing_data
            with open('save_username_password_email.json' , 'w') as wfile:
                json.dump(new_data , wfile , indent=4)
                wfile.close()

                


#===============================================================

#Function for making new project in mainpage of App=============
def Creat_new_project(datalist):
    
    while True:
        member_list = []
        for i in new_project.members:
            member_list.append(i['username'])
        print("Fill ito make project")
        print(f"1_Name of project :{new_project.name}")
        print(f"2_Set member for your project {member_list}")
        print("3_Save")
        print("4_exit")

        chosen_option = input('Choose :')

        if chosen_option == '1':
           projectname = name_project()

        elif chosen_option == '2':
            Add_member()
        elif chosen_option == '3':
            save_my_project(datalist)
        elif chosen_option == '4':
            break






#===============================================================

    



def Work_inside_Trellomize(datalist):
    while True:
        print('Choose a number & (*) to exit')
        print('1_Creat new project')
        print("2_View all projects")
        print('3_View projects you lead')
        print("4_View projects you're asignees")

        chosen_option = input("Choose your option")

        if chosen_option == '*':
            break
        
        elif chosen_option == '1':
            Creat_new_project(datalist)
