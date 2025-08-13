from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

def banner():
    console.print(Panel.fit("🏰 [bold cyan]Dungeon Escape[/bold cyan] 🏰", style="bold magenta"))

def message(text, style="white"):
    console.print(Text(text, style=style))

def show_stats(player):
    table = Table(title="Player Stats", style="bold green")
    table.add_column("Name", justify="center")
    table.add_column("HP", justify="center")
    table.add_column("Attack", justify="center")
    table.add_row(player.name, str(player.hp), str(player.attack))
    console.print(table)

def show_inventory(items):
    table = Table(title="Inventory", style="bold yellow")
    table.add_column("Item", justify="center")
    table.add_column("Effect", justify="center")
    for i in items:
        table.add_row(i.name, i.effect)
    console.print(table)