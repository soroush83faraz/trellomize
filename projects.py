from rich.console import Console
import json
from printing import *
import tasks
console = Console()


class Projects:
    ID = None
    name = None
    leader = None
    members_usernames = []
    tasks = []
    

    def __init__(self , name , leader):
        self.name = name
        self.leader = leader

    def make_dict_of_project(self):
        dicted_project = {'ID' : self.ID , 'name' : self.name , 'leader' : self.leader , 'members' : self.members_usernames , 'tasks' : self.tasks}
        return dicted_project

    def name_project(self):
        console.print('Enter a title for your project  😊' , justify='center' , style= 'violet bold')
    
        while True:
            title = input('                                                                                 Title :')
            if title == '*':
                break
            else:
                self.name = title
                break

    def Add_member(self , In_account_user):
        while True:
            Added = False
            console.print("Enter member's name who you wanna add :" , justify='center' , style='green')
            member_name = input('                                                                                 Member name :')
            if member_name == '*':
                break
            elif member_name == In_account_user.username:
                console.print(f'{In_account_user.username} is leader of the project' , justify='center' , style='red bold italic')
                break
            try: 
                with open('save_username_password_email.json' , 'r') as rfile:
                    data = json.load(rfile)
                    rfile.close()
            except:
                data = []
        
            for i in data:
                if i['username'] == member_name:
                    self.members_usernames.append(i['username'])
                    self.append(i['username'])
                    Added = True
                    console.print(f"[blue]{member_name}[/] [green]was added to project successfully[/]  ✅" , justify='center')
            
                
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
                console.print("The username was not found  🥲" , style='red' , justify='center')


    def get_ID(self , In_account_user):
        console.print("You should enter an unique [red]ID[/] for your project" , style='italic purple' , justify='center')
        while True:
            ID = input("                                                                                 ID :")

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
                console.print("Choose an unique [red]ID[/]" , justify='center' , style='green italic')
            else:
                self.ID = ID
                print('ID set')
                break

    def save_my_project(self , In_account_user):
        proj_ID = []
        if self.name == None:
            console.print("You should pick a title for your project" , justify='center')
        elif self.ID == None:
            console.print("You should pick an ID for your project" , justify='center')
    
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

        if self.ID in proj_ID:
            return

        else:
            members_name = []
            for username in self.members_usernames:
                members_name.append(username)

            self.leader = In_account_user.username
        
            # with open("Projects.json" , 'w') as wfile:
            #     project_dict = {'title' : new_project.name , "members" : members_name, "ID" : new_project.ID , "leader" : new_project.leader , "tasks" : new_project.tasks}
            #     json.dump(project_dict , wfile , indent=4)
            #     wfile.close()
        
            In_account_user.projects_leads.append(self.make_dict_of_project())

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
                    user['projects_member'].append(self.make_dict_of_project())

            with open('save_username_password_email.json' , 'w') as wfile:
                json.dump(user_info , wfile , indent=4)
                wfile.close()

    def finding_projects_leads (self) :
    
        try :
            with open("save_username_password_email.json" , "r") as json_file :
                users_info = json.load(json_file)
                json_file.close()
            
            
        except FileNotFoundError:
            users_info = []
        
        proj_path = [] 
        for user in range(len(users_info)) :
            if users_info[user]['username'] == self.leader:
                for item in range(len(users_info[user]["projects_leads"])) :
                    if users_info[user]["projects_leads"][item]["ID"] == self.ID :
                        proj_path.append(user)
                        proj_path.append("projects_leads")
                        proj_path.append(item)
                        proj_path.append("tasks")
                        #print(proj_path)
                        return proj_path

    def create_new_task (self) :
    
        proj_path_leads = self.finding_projects_leads()
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
            

