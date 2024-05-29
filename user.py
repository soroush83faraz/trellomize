import json
import logging
from rich.console import Console
from printing import *
console = Console()
import bcrypt
import base64

def hash_password(password):
    
    salt = bcrypt.gensalt()
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    encoded_hashed_password = base64.b64encode(hashed_password).decode('utf-8')
    return encoded_hashed_password

class User:
    """
    User class representing a person.
    Attributes:
        username (str): The person's name.
        password (int): The person's password.
        email (str): The person's gmail.
        IsActive (bool): The person's state.
        projects_member (list): The person's project's that he is a member.
        projects_leads (list): The person's project's that he is a leader.   
    functions :
    
         
    """
    username = None
    password = None
    email = None
    IsActive = True
    projects_member = []
    projects_leads = []

    def __init__(self , username , password , email , IsActive , projects):
        self.username = username
        self.password = password
        self.email = email
        self.IsActive = IsActive
        self.projects = projects

    def save_account(self):

        try:
            with open('save_username_password_email.json' , 'r') as reading_file:
                existing_data = json.load(reading_file)
        except:
            existing_data = []


        new_data = {"username" : self.username , "password" : hash_password(self.password) , "email" : self.email , 'projects_leads' : [] , 'projects_member' : [] , 'IsActive' : True}

        existing_data.append(new_data)

        with open('save_username_password_email.json' , 'w') as writing_file:
            json.dump(existing_data , writing_file , indent=4)

    
        logging.info(f"An account was made by {self.username} in save_account function and was saved in save_username_password_email.json")
    
        console.print('Your Account was saved successfully  ✅✌️'  , style='green' , justify= 'center')


    def remove_project(self):
        try:
            with open('save_username_password_email.json' , 'r') as file:
                users_info = json.load(file)
                file.close()
        except:
            users_info = []

        lines_list = []
        for user in users_info:
            if user['username'] == self.username:
                for project in self.projects_leads:
                    lines_list.append(project["ID"])
   
        chosen_project = pro_print(lines_list)
        Chosen_ID = lines_list[int(chosen_project)-1]

        for user in users_info:
            for project in user['projects_leads']:
                if project['ID'] == Chosen_ID:
                    user['projects_leads'].remove(project)
            
            for project in user['projects_member']:
                if project['ID'] == Chosen_ID:
                    user['projects_member'].remove(project)

        with open('save_username_password_email.json' , 'w') as file:
            json.dump(users_info , file , indent=4)
            file.close()
        