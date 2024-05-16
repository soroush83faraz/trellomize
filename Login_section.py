import json
import logging
from printing import *


logging.basicConfig(filename="mylog.log", level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

#FUnction for checking if a combination is valid or not==============
def check_combinations(username , password):
    data_list = {}
    with open('save_username_password_email.json' , 'r') as file:
        reader_list = json.load(file)
        file.close()


        for row in reader_list:
            if username == row['username'] and password == row['password']:
                data_list = row 
                break
    
    logging.info(f"{username} was logged in his account")

    return data_list

    
                

#====================================================================
#Function That you should log in with this===========================
def Log_in():
    datalist = []
    username = None
    password = None
    while True:
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
            if len(check_combinations(username , password)) != 0:
                datalist = check_combinations(username , password)
                console.print(f'[green]Welcome dear [bold][italic]{username}[/][/] to Trellomize[/]  😊💪' , justify='center')
                break
            else:
                console.print("The username-password combination doesn't exist  ❌" , justify='center' , style='darkgreen italic')
                logging.warning(f"{username} tried to log in with false informations")
        elif Choice == '4':
            break      

    return datalist
                
                
                

            
#====================================================================

