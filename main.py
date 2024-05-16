from making_new_account import *
from Login_section import *
from Trellomize_space_when_Log_in import *
import 
if __name__ == "__main__":

    while True:

        print("Welcome to trellomize \n What do you want to do?")
        print("1_Sign_up")
        print("2_Log_in")
        print('3_Finish')
    
        Choice = input('Enter your choice :')
        if Choice == '1':
            make_an_account()
        elif Choice == '2':
            datalist = Log_in()
            
            if len(datalist) != 0:
                Work_inside_Trellomize(datalist)
        



