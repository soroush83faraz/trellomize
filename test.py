# import json


# try :
#     with open("save_username_password_email.json" , "r") as json_file :
#         users_info = json.load(json_file)
#         json_file.close
            
            
# except FileNotFoundError:
#    users_info = []

# print(users_info)


from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Initialize the console
console = Console()

# Create custom text
custom_text = Text("Hello, this is a custom box!", style="bold magenta")

# Create a panel (box) with the custom text
panel = Panel(
    custom_text,
    title="Custom Box",  # Title of the panel
    title_align="center",  # Title alignment
    border_style="bright_green",  # Border color
    expand=True  # Do not expand the panel to fill the console width
)

# Print the panel to the console
console.print(panel)
