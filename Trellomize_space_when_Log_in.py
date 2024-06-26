import json
from projects import *
from tasks import * 
from user import *
from in_project_workplace import *
from printing import *
from go_to_project_for_leader import *
from go_to_project_for_member import *
import os


new_project = Projects(None , None)
In_account_user = User(None , None , None , None , None)
pre_list_of_members = []

def cpp_cls():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
#Function for making new project in mainpage of App=============
def Creat_new_project():
    
    """
    Creates a new project within the Trellomize application.

    Displays prompts to the user for entering project details such as title, members, and ID.
    Allows the user to save the project or exit the creation process.

    """
    
    logging.info("Arrived in Creat_new_project() in Trellomize_space_when_log_in.py")
    while True:
        member_list = []
        for i in new_project.members_usernames:
            member_list.append(i)
        console.print(f"[blue]Dear[/] [green]{In_account_user.username}[/] [blue]Fill it to make project[/]  😊" , justify='center')

        lines_list = [f"1_Project's title:{new_project.name}" , f"2_Project's members {member_list}" , f"3_Project's ID :{new_project.ID}" , "4_Save" , "5_exit"]

        chosen_option = pro_print(lines_list)

        if chosen_option == '1':
            new_project.name_project()

        elif chosen_option == '2':
            logging.critical(f"Add_member() called in Trellomize_space_when_log_in.py")
            new_project.Add_member(In_account_user)
        elif chosen_option == '3':
            logging.critical(f"get_ID() called in Trellomize_space_when_log_in.py")
            new_project.get_ID(In_account_user)
        elif chosen_option == '4':
            logging.critical(f"save_my_project() called in Trellomize_space_when_log_in.py")
            new_project.save_my_project(In_account_user)
        elif chosen_option == '5':
            break

#===============================================================

def Work_inside_Trellomize(datalist):
    
    """
    Handles user interaction within the Trellomize application.

    Args:
        datalist (dict): A dictionary containing user data, including username, password, email, projects_leads, and projects_member.
    """
    logging.info("Arrived in Work_inside_Trellomize()")
    In_account_user.username = datalist['username']
    In_account_user.password = datalist['password']
    In_account_user.email = datalist['email']
    In_account_user.projects_leads = datalist['projects_leads']
    In_account_user.projects_member = datalist['projects_member']



    while True:
        cpp_cls()
        console.print(f'Dear [green][italic]{In_account_user.username}[/][/] Choose a number & [red](*)[/] to exit' , justify='center')
        

        lines_list = ['1_Creat new project' ,"2_View all projects" , "3_Remove a project"]


        chosen_option = pro_print(lines_list)

        if chosen_option == '*':
            break
        
        elif chosen_option == '1':
            cpp_cls()
            logging.critical(f"Creat_new_project() called in Work_Inside_Trellomize() in Trellomize_space_when_Log_in.py")
            Creat_new_project()

        elif chosen_option == '2':
            cpp_cls()
            logging.critical(f"show_all_projects() called in Work_Inside_Trellomize() in Trellomize_space_when_Log_in.py")
            show_all_projects()

        elif chosen_option == '3':
            logging.critical(f"In_account_user.remove_project() called in Trellomize_space_when_Log_in.py")
            In_account_user.remove_project()


def show_all_projects():
    """
    Displays a list of projects available to the user.

    Reads user information from a JSON file named "save_username_password_email.json".
    Retrieves the projects led by the user and the projects they are a member of.
    Displays project names along with their status (leader/member).

    """

    logging.info("Arrived in show_all_projects() in Trellomize_space_when_log_in.py")
    try:
        with open('save_username_password_email.json' , 'r') as file:
            users_info = json.load(file)
            file.close()
    except:
        users_info = []

    counter = 1

    project_leads_counter = 0
    proj_list = []
    proj_show = []
    for user in users_info:
        if user['username'] == In_account_user.username:
            for project in user['projects_leads']:
                # console.print(f"{counter}_{project['name']}    (leader)" , justify='center')
                proj_list.append(project)
                proj_show.append(f"{counter}_{project['name']}    (leader)")
                counter += 1
                project_leads_counter += 1
            for proj in user["projects_member"]:
                # console.print(f"{counter}_{proj['name']}       (member)" , justify='center')
                proj_list.append(proj)
                proj_show.append(f"{counter}_{proj['name']}       (member)")
                counter += 1
        
    
    
    
    while True:
        if len(proj_list) > 0:
            console.print('Which project?' , justify='center' , style='cyan bold')
            proj_number = pro_print(proj_show)
            if proj_number == '*':
                break
            if int(proj_number) > 0 and int(proj_number) <= project_leads_counter:
                logging.critical(f'start({proj_list[int(proj_number)-1]['ID']} , {In_account_user.username}) called in Trellomize_space_when_Log_in.py')
                start(proj_list[int(proj_number)-1]['ID'] , In_account_user.username )
            elif int(proj_number) > project_leads_counter and int(proj_number) < counter:
                logging.critical(f"start_for_member({proj_list[int(proj_number)-1]['ID']} , { In_account_user.username } ) called in Trellomize_space_when_Log_in.py")
                start_for_member(proj_list[int(proj_number)-1]['ID'] , In_account_user.username )
        else:
            console.print("There isn't any project to show" , justify='center' , style='violet bold')
            break
