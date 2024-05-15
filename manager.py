import json
from rich.console import Console
from rich.text import Text
import os
import argparse

con = Console()
parser = argparse.ArgumentParser()

def main () :
    parser.add_argument("function_name" , nargs=1 , type=str , help="calls the function name if there is one" )
    parser.add_argument("--password" , nargs=1 , type=str , help="gets password" )
    parser.add_argument("--username" , nargs=1 , type=str , help="gets username" )
    args = parser.parse_args()
    clear()

    # print(f"username : {args.username} and {args.function_name}")
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
    with open('admin.json' , 'w') as json_file:
        json.dump(None, json_file)
        con.print("no more data" , style="blue")
               
def clear():
    os.system('cls')
    
if __name__ == "__main__":
    main()


    
        
