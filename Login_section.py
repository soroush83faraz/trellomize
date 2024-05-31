import json
import logging
from printing import *
import bcrypt
import base64
def check_password(password, encoded_hashed_password):
    # Decode the Base64 string to get the original hashed password
    hashed_password = base64.b64decode(encoded_hashed_password)
    # Verify the password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


logging.basicConfig(filename="mylog.log", level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

#FUnction for checking if a combination is valid or not==============
def check_combinations(username , password):
    
    """
    Validates the combination of a username and password.

    Args:
        username (str): The username to check.
        password (str): The password to check.

    Returns:
        dict: A dictionary containing user data if the combination is valid, otherwise an empty dictionary.

    """
    
    data_list = {}
    with open('save_username_password_email.json' , 'r') as file:
        reader_list = json.load(file)
        file.close()


        for row in reader_list:
            if username == row['username'] and check_password(password, row['password']):
                data_list = row 
                break
    
    logging.info(f"{username} was logged in his account")
    logging.warning(f"check_combinations() returns{data_list}")
    return data_list

    
                

#====================================================================
#Function That you should log in with this===========================
def Log_in():
    
    """
    Allows users to log in by entering their username and password.

    Returns:
        list: A list containing user data (e.g., username, email, etc.) upon successful login.

    """
    
    datalist = []
    username = None
    password = None
    while True:
        clear_terminal()
        console.print('Enter [red]*[/] if you wanna exit each section' , justify='center' , style='violet bold')
        lines_list = [f'1_username :{username}' , f'2_password :{password}' , '3_Log_in' , '4_Exit']
        Choice = pro_print(lines_list)

        if Choice == '1':
            while True:
                username = input('                                                                                 Username :')
                if username == '*':
                    username = None
                    break
                break
        elif Choice == '2':
            while True:
                password = input('                                                                                 password :')
                if password == '*':
                    password = None
                    break
                break
        elif Choice == '3':
            try:
                with open('save_username_password_email.json' , 'r') as file:
                    users_info = json.load(file)
                    file.close()
            except:
                users_info = []
            booleanIsActive = True
            for user in users_info:
                if user['username'] == username:
                    booleanIsActive = user['IsActive']
            if booleanIsActive == False:
                console.print("You are banned by admin of server" , justify='center' , style='red bold')
                a = input('                                                                              enter sth : ')
            elif len(check_combinations(username , password)) != 0 and booleanIsActive:
                
                datalist = check_combinations(username , password)
                console.print(f'[green]Welcome dear [bold][italic]{username}[/][/] to Trellomize[/]  😊💪' , justify='center')
                break
            
            else:
                console.print("The username-password combination doesn't exist  ❌" , justify='center' , style='green italic')
                logging.warning(f"{username} tried to log in with false informations")
        elif Choice == '4':
            break      
    logging.warning(f"Log_in() returns {datalist}")
    return datalist
                
                
                

            
#====================================================================

