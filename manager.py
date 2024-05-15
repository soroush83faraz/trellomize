import json
import os
import argparse

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
        print("you are deleting everything , are you sure ?")
        while check != "NO" and check != "YES" :

            check = input("if you are sure type (YES) and if you are not type (NO)")
            if check == "yes" :
                print("you should type it in capital letter.")
                check = input("if you are sure type (YES) and if you are not type (NO)")
            elif check == "YES" :
                purge_data()
            elif check == "NO" :
                print()

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
            print(data)
    else :
        print("you dont have the acces to make an admin")
            
            
        
def purge_data () :
    with open('admin.json' , 'w') as json_file:
        json.dump(None, json_file)
        print("no more data")
               
def clear():
    os.system('cls')
    
if __name__ == "__main__":
    main()


    
        
