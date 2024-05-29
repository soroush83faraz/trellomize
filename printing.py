from rich.console import Console
import os
import logging
console = Console()

logging.basicConfig(filename="mylog.log", level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def pro_print(lines_list):
    
    """
    Displays a list of options and allows the user to choose one.

    Args:
        lines_list (list): A list of strings representing the available options.

    Returns:
        str: The chosen option (or '*' if the user cancels).
    """
    
    line = 1
    while True:
        for strnum in range(len(lines_list)):
            if strnum == line-1:
                console.print(f"{lines_list[strnum]} 👈" , style="cyan bold italic" , justify='center')
            else:
                console.print(f"{lines_list[strnum]}" , justify='center')

        console.print('[bold][violet]Move to the section you want[/][/] with [cyan][italic](w , a , s , d)[/][/] and "c" for choose' , justify='center')
        console.print()
        choice = input("                                                                                 Move :")
        if choice == '*':
            return '*'
        elif choice == 'w' and line > 1:
            line -= 1
        elif choice == 's' and line < len(lines_list):
            line += 1
        elif choice == 'c':
            logging.info('Returned from pro_print function')
            return str(line)
        clear_terminal()