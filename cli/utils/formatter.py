from rich.console import Console
from rich.table import Table

console = Console()

class Formatter:
    @staticmethod
    def display(data):
        table = Table(title=f"✨ {data['title'].upper()} ✨", show_header=True, header_style="bold magenta")
        table.add_column("Key/ID", style="dim", width=10)
        table.add_column("Details Summary")
        
        for key, value in data["items"].items():
            table.add_row(key, str(value))
            
        console.print(table)