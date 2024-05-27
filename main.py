from making_new_account import *
from Login_section import *
from Trellomize_space_when_Log_in import *
from rich.console import Console
from printing import *
from go_to_project_for_leader import *
import logging
logging.basicConfig(filename="mylog.log", level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

if __name__ == "__main__":

    while True:

        console.print("Welcome to trellomize \n What do you want to do?" , style='blue bold italic' , justify='center')
        lines_list = ["1_Sign_up" , "2_Log_in" , "3_Finish"]
        logging.info('Calling proprint function in main')
        line = pro_print(lines_list)
        
        if line == '1':
            logging.critical(f"make_an_account() called in main.py")
            make_an_account()
        elif line == '2':
            logging.critical("Log_in() called in main.py")
            datalist = Log_in()
            if len(datalist) != 0:
                logging.critical("Work_inside_trellomize() called in main.py")
                Work_inside_Trellomize(datalist)
        elif line == '3':
            break
        



