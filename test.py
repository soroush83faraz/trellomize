from rich.console import Console
from rich.table import Table
console = Console()

console.print('This is the same text')
console.print('This is the same text' , style='bold')
console.print('[bold]This is the [cyan]same text[/][/]')
console.print(":apple: :thumbs_up:")




