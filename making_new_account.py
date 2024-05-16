import json
from validate_email_address import validate_email
import logging
from user import *
user = User(None , None , None , None , None)
logging.basicConfig(filename="mylog.log", level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
#1 : emailaddress in not valid \ 2 : emailaddress is used \ 7 : emailaddress is correct
def my_validate_email():
    print('Enter a standard form of emailaddress and if you wanna exit enter *')
    while True:
        problem = False
        emailaddress = input('Email :')
        if emailaddress == '*':
            return None
        if not validate_email(emailaddress):
            print('you should enter standard form like : firstname.lastname@example.com')
            problem = True
       
        try :
            with open('save_username_password_email.json') as reading_file:
                reader_dict = json.load(reading_file)
                existing_email = []
                for i in reader_dict['email']:
                    existing_email.append(i)
        except:
            existing_email = []

        if emailaddress in existing_email:
            print('this email is used')
            problem = True
    
        if not problem:
            print("Emailaddress was accepted")
            break
    return emailaddress
#==============================================================================
#Function for checking if username just include alphabet and numbers===========
def alpha_or_num(username):
    alphanum = 0
    numnum = 0
    for letter in username:
        if letter.isalpha(): alphanum += 1
        elif letter.isdigit(): numnum += 1

    if (alphanum + numnum) == len(username):
        return True

    return False
#==============================================================================
#Functiom for finding forbidden chatacter for password=========================
def find_strange(password):
    checklist = ['@', '#' , '$' , '&']
    for letter in password:
        if not letter.isalpha() and not letter.isdigit() and letter not in checklist:
            return  letter

    return None


#==============================================================================
#Section for validating username===============================================
def validating_username():
    while True:
        problem = False
        print("Username must include at least 5 letter or number \t if you wanna Exit enter *")
        username = input("Username :")
        if username == '*':
            return None
        if len(username) < 5:
            print('Your username must at least include 5 letters')
            problem = True
        if  ' ' in username:
            print("Your username musn't include space")
            problem = True
        if not alpha_or_num(username):
            print("Your username must include just number and alphabetical letter")
            problem = True
        try: 
            with open('save_username_password_email.json' , mode='r') as reading_file:
                username_dict = json.load(reading_file)
                existing_username = []
                for i in username_dict:
                    existing_username.append(i)
            reading_file.close()

        except:
            existing_username = []

        if username in existing_username:
            print('This username is used')
            problem = True
        if not problem:        
            print("Username was acceped")
            break
    return username
        
#==============================================================================
def IsPasswordValid():
    checklist = ['@' , '#' , '$' , '&']
    
    print('Your password should include at least 8 letter and must be combination of letter number and a character like @,#,$,& \t if you wanna exit enter *')
    while True:
        checklist_number = 0
        problem = False
        password = input("Password :")
        if password == '*':
            return None
        if len(password) < 8:
            print('your password should be longer')
            problem = True
        for letter in password:
            if letter in checklist:
                checklist_number += 1
        if checklist_number == 0:
            print("Your password must include at least one of @ ,# ,$ ,&")
            problem = True
        if len(password) > 16:
            print('Your password must be less then 16 letter')
            problem = True
        Strange_letter = find_strange(password)
        if Strange_letter != None:
            print(f'{Strange_letter} is forbidden')
            problem = True
        if not problem:
            print('Password accepted')
            break

    return password            

        
#Section for saving data in CSV format=========================================
def save_account():
    try:
        with open('save_username_password_email.json' , 'r') as reading_file:
            existing_data = json.load(reading_file)
    except:
        existing_data = []

    new_data = {"username" : user.username , "password" : user.password , "email" : user.email , 'projects_leads' : [] , 'projects_member' : []}

    existing_data.append(new_data)

    with open('save_username_password_email.json' , 'w') as writing_file:
        json.dump(existing_data , writing_file , indent=4)

    
    logging.info(f"An account was made by {user.username} in save_account function and was saved in save_username_password_email.json")
    
    print('Your Account was saved successfully')
#==============================================================================



def make_an_account():
    print('For making an account in trellomize you should pick username , password and emailaddress')

    user.username = None
    user.password = None
    user.email = None
    while True:
        print("Here is the status of data:")
        print(f"1_Username :{user.username}")
        print(f"2_Password :{user.password}")
        print(f"3_EmailAddress :{user.email}")
        print('4_Save')
        print('5_Exit')
        print('\n')
        print("What do you want to do?(1,2,3,4,5)")

        

        Option = input('Option :')

        if Option == '1':
           user.username =  validating_username()
        elif Option == '2':
           user.password = IsPasswordValid()
        elif Option == '3':
           user.email = my_validate_email()
        elif Option == '4':
            if user.username != None and user.password != None and user.email != None:
                save_account()
                break
            else:
                print('Some field is empty')
        elif Option == '5':
            break



        
    