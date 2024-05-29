import json
import logging
from rich.console import Console
from printing import *
console = Console()
import bcrypt
import base64

def hash_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Encode the hashed password to a Base64 string
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


   