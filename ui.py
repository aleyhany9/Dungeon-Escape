from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def banner():
    console.print(Panel.fit("[bold yellow]🏰 DUNGEON ESCAPE 🏰[/bold yellow]\n[italic cyan]Find your way out... if you can[/italic cyan]"))

def status_panel(player):
    console.print(Panel(f"[bold]Name:[/bold] {player.name}\n[red]HP:[/red] {player.hp}\n[green]Gold:[/green] {player.gold}"))

def room_description(room):
    console.print(Panel(f"[bold cyan]{room.name}[/bold cyan]\n{room.description}"))

def inventory_table(items):
    table = Table(title="Inventory")
    table.add_column("Item", style="yellow")
    table.add_column("Effect", style="green")
    for item in items:
        table.add_row(item.name, item.effect)
    console.print(table)

def message(text, style="white"):
    console.print(f"[{style}]{text}[/{style}]")
