from making_new_account import *
from Login_section import *
from Trellomize_space_when_Log_in import *
from rich.console import Console
from printing import *
from go_to_project_for_leader import *


if __name__ == "__main__":

    while True:

        console.print("Welcome to trellomize \n What do you want to do?" , style='blue bold italic' , justify='center')
        lines_list = ["1_Sign_up" , "2_Log_in" , "3_Finish"]
        line = pro_print(lines_list)
        
        if line == '1':
            make_an_account()
        elif line == '2':
            datalist = Log_in()
            if len(datalist) != 0:
                Work_inside_Trellomize(datalist)
        



