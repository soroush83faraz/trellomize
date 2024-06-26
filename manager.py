import json
from rich.console import Console
from rich.text import Text
import os
import argparse

con = Console()
parser = argparse.ArgumentParser()

def main () :
    """
    Entry point for your program.

    Parses command-line arguments and executes the specified function.

    """
    
    parser.add_argument("function_name" , nargs=1 , type=str , help="calls the function name if there is one" )
    parser.add_argument("--password" , nargs=1 , type=str , help="gets password" )
    parser.add_argument("--username" , nargs=1 , type=str , help="gets username" )
    # parser.add_argument("--changefield" , nargs=1 , type=str , help="get field")
    args = parser.parse_args()
    clear()

    # print(f"username : {args.username} and {args.function_name}")
    if args.function_name[0] == "change-field" :
    
        try :
            with open('admin.json' , 'r') as json_file :
                input_from_json = json.load(json_file)     
        except :
            input_from_json = []
        try :
            with open('save_username_password_email.json' , 'r') as json_file :
                inputjson = json.load(json_file)     
        except :
            inputjson = None
        
        if input_from_json["password"] == args.password[0] and input_from_json["username"] == args.username[0]:
            if inputjson != None:   
                while True :
                    show_is_active()
                    username = input("username : ")
                    try :
                        with open('save_username_password_email.json' , 'r') as json_file :
                            input_from_json = json.load(json_file)     
                    except :
                        input_from_json = []

                    for user in input_from_json :
                        if username == user["username"] :
                            changing_is_active(username)
                            return
            else :
                con.print("there are no user to edit" ,  style="bold")
        else :
            clear()
            con.print("you dont have the [bold yellow]acces[/bold yellow] to change field")              
        

    if args.function_name[0] == "create-admin" :
        create_admin(args.username[0] , args.password[0])
    if args.function_name[0] == "purge-data" :
        check = ""
        con.print("you are deleting everything , are you [underline]sure[/underline] ?" , style="bold")
        while check != "NO" and check != "YES" :
            con.print("\nif you are sure type ([bold green]YES[/bold green]) and if you are not type ([bold red]NO[/bold red]) :")
            check = input()
            clear()
            if check == "yes" :
                clear()
                con.print("you should type it in [underline]capital[/underline] letter.\n")   
                con.print("\nif you are sure type ([bold green]YES[/bold green]) and if you are not type ([bold red]NO[/bold red]) :")
                check = input()
            if check == "YES" :
                purge_data()
            if check == "NO" :
                print()
            if check != "YES" and check != "NO" :
                con.print("your choice is not valid type [bold green]YES[/bold green] or [bold red]NO[/bold red]")   

                

def create_admin(username , password) :
    
    """
    Creates an admin account with the specified username and password.

    Args:
        username (str): The desired username for the admin account.
        password (str): The desired password for the admin account.
    """
    
    data = {"username" : username , "password": password}
   
    try :
        with open('admin.json' , 'r') as json_file :
            input_from_json = json.load(json_file)     
    except :
        input_from_json = []
        

        
    if input_from_json == None :    
        with open('admin.json' , 'w') as json_file:
            json.dump(data, json_file)
            con.print(data)
    else :
        clear()
        con.print("you dont have the [bold yellow]acces[/bold yellow] to make an admin")
            
            
        
def purge_data () :
    
    """
    Purges data by writing `None` to two JSON files: 'admin.json' and 'save_username_password_email.json'.
    """
    
    with open('admin.json' , 'w') as json_file:
        json.dump(None, json_file)
        con.print("no more data" , style="blue")
    with open('save_username_password_email.json' , 'w') as json_file:
        json.dump( [], json_file)
              
def show_is_active () :
    
    """
    Displays the username and whether the user is active or not.

    Reads user information from a JSON file named "save_username_password_email.json".
    If the file doesn't exist or is empty, it assumes no users are active.

    """
    
    try :
        with open ("save_username_password_email.json" , "r") as json_file :
            user_info = json.load(json_file)
            json_file.close()
                
    except :
        user_info = None
    if user_info != None :  
        for user in user_info :
            print(user["username"] , "IsActive =" , user["IsActive"] )    
        
def changing_is_active (username) :
    
    """
    Toggles the 'IsActive' status of a user account.

    Args:
        username (str): The username of the account to modify.

    Note:
        - This method modifies the 'IsActive' attribute in user data.
        - If the account is currently active, it will be deactivated, and reverse.

    """
    
    try :
        with open ("save_username_password_email.json" , "r") as json_file :
            user_info = json.load(json_file)
            json_file.close()
                
    except :
        user_info = None
        
    if user_info != None :
        for user in user_info :
            if user["username"] == username :
                if user["IsActive"] == True :
                    user["IsActive"] = False
                    print(f"{username} Is Deactive")
                else :
                    user["IsActive"] = True
                    print(f"{username} Is Active")
                with open('save_username_password_email.json' , 'w') as json_file:
                    json.dump(user_info, json_file , indent = 4)               
        
    
    
    
        
               
def clear():
    """
    Clears the terminal screen.
    """
    os.system('cls')
    
if __name__ == "__main__":
    main()


    
        
