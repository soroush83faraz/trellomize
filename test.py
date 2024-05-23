# import json


# try :
#     with open("save_username_password_email.json" , "r") as json_file :
#         users_info = json.load(json_file)
#         json_file.close()
            
            
# except FileNotFoundError:
#    users_info = []

# print(users_info)

import curses

def pro_print(stdscr, lines_list):
    # Initialize curses colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Selected line color
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal line color

    # Turn off echoing of keys to the screen
    curses.noecho()
    
    # React to keys instantly without waiting for Enter to be pressed
    curses.cbreak()
    
    # Enable keypad mode to capture special keys
    stdscr.keypad(True)

    line = 1

    while True:
        stdscr.clear()

        # Display the lines
        height, width = stdscr.getmaxyx()
        for strnum in range(len(lines_list)):
            if strnum == line - 1:
                stdscr.addstr(strnum, width // 2 - len(lines_list[strnum]) // 2, f"{lines_list[strnum]} 👈", curses.color_pair(1) | curses.A_BOLD | curses.A_UNDERLINE)
            else:
                stdscr.addstr(strnum, width // 2 - len(lines_list[strnum]) // 2, lines_list[strnum], curses.color_pair(2))

        # Display the instructions
        instructions = '[Use arrow keys to move and Enter to choose]'
        stdscr.addstr(len(lines_list) + 1, width // 2 - len(instructions) // 2, instructions)

        stdscr.refresh()

        # Wait for user input
        choice = stdscr.getch()

        # Handle user input
        if choice == ord('*'):
            return '*'
        elif choice == curses.KEY_UP and line > 1:
            line -= 1
        elif choice == curses.KEY_DOWN and line < len(lines_list):
            line += 1
        elif choice == curses.KEY_ENTER or choice in [10, 13]:  # Enter key
            return str(line)

def main():
    lines_list = [
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4"
    ]
    result = curses.wrapper(pro_print, lines_list)
    print(f"You selected option {result}")

if __name__ == "__main__":
    main()
