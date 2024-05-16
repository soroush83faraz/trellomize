import json
import logging

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
        print(f'1_username :{username}')
        print(f'2_password :{password}')
        print('3_Log_in')
        print('4_Exit')
        print('Enter * if you wanna exit each section')
        Choice = input('Choice :')

        if Choice == '1':
            while True:
                username = input('Username :')
                if username == '*':
                    username = None
                    break
                break
        elif Choice == '2':
            while True:
                password = input('password :')
                if password == '*':
                    password = None
                    break
                break
        elif Choice == '3':
            if len(check_combinations(username , password)) != 0:
                datalist = check_combinations(username , password)
                print(f'Welcome dear {username} to Trellomize')
                break
            else:
                print("The username-password combination doesn't exist")
                logging.warning(f"{username} tried to log in with false informations")
        elif Choice == '4':
            break      

    return datalist
                
                
                

            
#====================================================================

