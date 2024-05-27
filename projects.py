from rich.console import Console
import json
from printing import *
from tasks import *
import tasks
import time
from datetime import datetime , timedelta
from history import *   
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
            try: 
                with open('save_username_password_email.json' , 'r') as rfile:
                    data = json.load(rfile)
                    rfile.close()
            except:
                data = []
        
            for user in data:
                console.print(user['username'] , justify='center' , style='red italic')

            Added = False
            console.print("Enter member's name who you wanna add :" , justify='center' , style='green')
            member_name = input('                                                                                 Member name :')
            if member_name == '*':
                break
            elif member_name == In_account_user.username:
                console.print(f'{In_account_user.username} is leader of the project' , justify='center' , style='red bold italic')
                break
            
            elif member_name in self.members_usernames:
                console.print('This has benn already added' , justify='center' , style='cyan bold')
                break

            for i in data:
                if i['username'] == member_name:
                    self.members_usernames.append(i['username'])
                    
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

    def finding_projects_member(self , username):
        try :
            with open("save_username_password_email.json" , "r") as json_file :
                users_info = json.load(json_file)
                json_file.close()
        except FileNotFoundError:
            users_info = []
        
        task_list = []
        for user in users_info:
            if user['username'] == username:
                for project in user['projects_member']:
                    if project['ID'] == self.ID:
                        for task in project['tasks']:
                            if username in task['Assignees']:
                                task_list.append(task)

        return task_list


    def add_task_to_other_user(self , task):
        try:
            with open('save_username_password_email.json' , 'r') as file:
                users_info = json.load(file)
                file.close()
        except:
            users_info = []
        
        for user in users_info:
            if user['username'] in self.members_usernames:
                for project in user['projects_member']:
                    if project['ID'] == self.ID:
                        dicted_task = task.make_dict_of_tasks()
                        project['tasks'].append(dicted_task)
        
     
        with open('save_username_password_email.json' , 'w') as file:
            json.dump(users_info , file , indent=4)
            file.close()
   
    def create_new_task (self):
        
        start_time = datetime.now()
        proj_path_leads = self.finding_projects_leads()
        Title = "Task"
        Description = "Put your discription here"
        Priority = "LOW"
        status = "BACKLOG"
        Assignees = []
        End_time = start_time + timedelta(hours = 24)
        while True :
            clear_terminal()
            console.print("[violet]Choose a number &[/] [red](*)[/] [violet]to exit[/]" , justify='center')
            lines_list = [f"1-Title : {Title}" , f"2-Description : {Description}" , f"3-Priority : {Priority}" , f"4-status :{status}" , f'5_Assignees{Assignees}' , f"6_End_time -> {End_time.strftime("%d/%m/%Y  %H:%M:%S")}" , f"7-save Task" , '8_Exit']
            choice = pro_print(lines_list)
        
            if choice == '8' :
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
                
            elif choice == "4" :
                status = input("                                                                                 status :")
                if status != "BACKLOG" and status != "TODO" and status != "DOING" and status != "DONE" and status != "ARCHIVED" :
                    console.print("[violet][bold]You should choose a status from[/][/][red][italic] (BACKLOG , TODO , DOING , DONE , ARCHIVED) [/][/]" , justify='center')
                    status = None
            elif choice == '5':
                for member in self.members_usernames:
                    console.print(f'[green]{member}[/]' , justify='center')
                console.print('Who do you wanna assign to this task' , justify='center' , style='blue bold')
                chosen_member = input("                                                                                 member's name:")
                if chosen_member in self.members_usernames:
                    Assignees.append(chosen_member)
                else:
                    console.print(f"[red][italic][bold]{chosen_member}[/][/][/] isn't member of the project" , justify='center')
            elif choice == '6':
                chosen_end_time = input("                                                                                 delta:")
                if int(chosen_end_time) > 0:
                    End_time = start_time + timedelta(hours  = int(chosen_end_time))
            elif choice == "7" :
                task = tasks.Task(Priority , Title , Description , status)
                task.assignees = Assignees
                task.start_time = start_time
                task.end_time = End_time

                fhistory = History()
                fhistory.date = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
                fhistory.content =  f"{self.leader} Made project: {self.name}"
                fhistory.doer = self.leader 

                task.history.append(fhistory.make_dict_of_history())
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
                    self.add_task_to_other_user(task)
                break
                
            else :
                print("your choice isnt valid please choose from 1 , 2 , 3 , 4 , 5")

    def add_proj_to_him(self ,usern):
        try:
            with open('save_username_password_email.json' , 'r') as file:
                users_info = json.load(file)
                file.close()
        except:
            users_info = []
            
        for user in users_info:
            if user['username'] == usern:
 
                for task in self.tasks:
                    if isinstance(task , Task):
                        dicted = task.make_dict_of_tasks()
                        self.tasks.remove(task)
                        self.tasks.append(dicted)
                user['projects_member'].append(self.make_dict_of_project())

                # for proj in user['projects_member']:
                #     for task in proj['tasks']:
                #         if isinstance(task , Task):
                #             dicted = task.make_dict_of_tasks()
                #             proj['tasks'].remove(task)
                #             proj['tasks'].append(dicted)

        with open('save_username_password_email.json' , 'w') as file:
            json.dump(users_info , file , indent=4)
            file.close()

    def update_members(self):
        try:
            with open('save_username_password_email.json' , 'r') as file:
                users_info = json.load(file)
                file.close()
        except:
            users_info = []

        
        for user in users_info:
            
            for project in user['projects_leads']:
                if project['ID'] == self.ID:
                    project['members'] = self.members_usernames
            for project in user['projects_member']:
                if project['ID'] == self.ID:
                    project['members'] = self.members_usernames
        
        
        with open('save_username_password_email.json' , 'w') as file:
            json.dump(users_info , file , indent=4)
            file.close()
        

        All_id_list = []
        for user in users_info:
            if user['username'] in self.members_usernames:
                for project in user['projects_member']:
                    All_id_list.append(project['ID'])
                
                if self.ID not in All_id_list:
                    self.add_proj_to_him(user['username'])
                All_id_list.clear()

    def remove_a_member(self):
        lines_list = []
        for member in self.members_usernames:
            lines_list.append(member)
        chosen_member = int(pro_print(lines_list))
        self.members_usernames.pop(chosen_member-1)
        self.update_members()

        try:
            with open('save_username_password_email.json' , 'r') as file:
                users_info = json.load(file)
                file.close()
        except:
            users_info = []

        for user in users_info:
            for project in user['projects_member']:
                if project['ID'] == self.ID and user['username'] not in self.members_usernames:
                    user['projects_member'].remove(project)
        
        with open('save_username_password_email.json' , 'w') as file:
            json.dump(users_info , file , indent=4)
            file.close()

    def show_all_members(self , user):
        for member in self.members_usernames:
            console.print(f"{member}" , justify='center' , style='red italic')

        lines_list = ["1_Remove a member" , "2_Add member"]
        Chosen_option = pro_print(lines_list)

        if Chosen_option == '1' and (user.username == self.leader):
            self.remove_a_member()
        elif Chosen_option == '2':
            self.Add_member(user)
            self.update_members()
            
    def update_project(self):
        try:
            with open('save_username_password_email.json' , 'r') as file:
                users_info = json.load(file)
                file .close()
        except:
            users_info = []


        
        for user in users_info:
            for project in user['projects_leads']:
                if project['ID'] == self.ID:
                    self.name = project['name']
                    self.ID = project['ID']
                    self.leader = project['leader']
                    self.members_usernames.clear()
                    for member in project['members']:
                        self.members_usernames.append(member)
                    self.tasks.clear()
                    for task in project['tasks']:
                        rtask = Task(None , None , None , None)
                        rtask.comments = task['Comments']
                        rtask.assignees = task['Assignees']
                        rtask.discription = task['Description']
                        rtask.end_time = task['End_time']
                        rtask.history = task['History']
                        rtask.ID = task['ID']
                        rtask.priority = task['Priority']
                        rtask.start_time = task['Start_time']
                        rtask.end_time = task['End_time']
                        rtask.status = task['Status']
                        rtask.title = task['Title']
                        self.tasks.append(rtask)
                break
            break

    def save_into_json(self):
        try:
            with open('save_username_password_email.json' , 'r') as file:
                users_info = json.load(file)
                file.close()
        except:
            users_info = []

        for user in users_info:
            for project in user['projects_leads']:
                if project['ID'] == self.ID:
                    project['leader'] = self.leader
                    project['members'] = self.members_usernames
                    project['name'] = self.name
                    project['tasks'].clear()
                    for task in self.tasks:
                        dected = task.make_dict_of_tasks()
                        project['tasks'].append(dected)
        for user in users_info:
            for project in user['projects_member']:
                if project['ID'] == self.ID:
                    project['leader'] = self.leader
                    project['members'] = self.members_usernames
                    project['name'] = self.name
                    project['tasks'].clear()
                    for task in self.tasks:
                        dected = task.make_dict_of_tasks()
                        project['tasks'].append(dected)
                    

        with open('save_username_password_email.json' , 'w') as file:
            json.dump(users_info , file , indent=4)
            file.close()
