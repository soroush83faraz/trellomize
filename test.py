# import json


# try :
#     with open("save_username_password_email.json" , "r") as json_file :
#         users_info = json.load(json_file)
#         json_file.close()
            
            
# except FileNotFoundError:
#    users_info = []

# print(users_info)
from datetime import datetime , timedelta
import time
now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

dt_string2 = now  + timedelta(hours=9)

dtstring3 = dt_string2.strftime("%d/%m/%Y  %H:%M:%S")
print(dt_string)
print(dtstring3)