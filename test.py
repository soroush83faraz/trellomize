# import json


# try :
#     with open("save_username_password_email.json" , "r") as json_file :
#         users_info = json.load(json_file)
#         json_file.close()
            
            
# except FileNotFoundError:
#    users_info = []

# print(users_info)

ls1 = [1,2,3,4]
ls2 = [11 , 22 , 33 , 44]
ls3 = [111 , 222 , 333 ,444]
ls4 = [1111 , 2222 , 3333 , 4444]

sRR = [[0, 0 , 0 , 0] for _ in range(4)]


for i in range(len(ls1)):
    sRR[i][0] = ls1[i]
for i in range(len(ls2)):
    sRR[i][1] = ls2[i]
for i in range(len(ls3)):
    sRR[i][2] = ls3[i]
for i in range(len(ls4)):
    sRR[i][3] = ls4[i]



print(sRR)