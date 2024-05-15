import json
import argparse

parser = argparse.ArgumentParser()

def main () :
    parser.add_argument("function_name" , nargs=1 , type=str , help="calls the function name if there is one" )
    parser.add_argument("--password" , nargs=1 , type=str , help="gets password" )
    parser.add_argument("--username" , nargs=1 , type=str , help="gets username" )
    args = parser.parse_args()
    

    # print(f"username : {args.username} and {args.function_name}")
    if args.function_name[0] == "create-admin" :
        create_admin(args.username[0] , args.password[0])
    # if args.function_name[0] == "purge-data" :
    #     create_admin(args.username[0] , args.password[0])
    
        

def create_admin(username , password) :
    data = {"username" : username , "password": password}

    with open('admin.json', 'w') as json_file:
        json.dump(data, json_file)
        print(data)







if __name__ == "__main__":
    main()


    
        
