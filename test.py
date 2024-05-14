import json

dict = {'username' : "Saeed" , 'password' : 'Saeedg00' , 'email' : "Saeed@gmail.com" , 'projects' : ['A' , 'B' , 'C']}

try: 
    with open('test.json' , 'r') as load_file:
        existing_dict = json.load(load_file)
    load_file.close()
except:
    existing_dict = []


with open('test.json' , 'w') as wfile:
    json.dump(existing_dict , wfile , indent=4)
    wfile.close()

for i in existing_dict :
    print(i['email'])

