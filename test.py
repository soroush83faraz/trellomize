import json

with open('save_username_password_email.json' , 'r') as file:

    data = json.load(file)

print(data[1])

