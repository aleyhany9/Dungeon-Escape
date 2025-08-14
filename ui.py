from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

def banner():
    console.print(
        Panel.fit(
            "[bold yellow]🏰 DUNGEON ESCAPE 🏰[/bold yellow]\n[dim]A retro text adventure[/dim]",
            border_style="magenta",
            box=box.DOUBLE,
        )
    )

def blurb_and_intro():
    console.print(Panel.fit(
        "[bold]Dungeon Escape[/bold] is a short, retro-style text adventure.\n"
        "Explore rooms, face mysterious events, and find your way out.\n"
        "[dim]Every choice could be your last...[/dim]",
        border_style="cyan",
        box=box.ROUNDED
    ))

    console.print(Panel(
        "You awaken in a damp, stone cell. Faint torchlight flickers.\n"
        "Rusty bars stand between you and the corridor beyond.\n"
        "Somewhere in the shadows, something moves...\n"
        "[bold]Goal:[/bold] Escape the dungeon.",
        title="[bold]Story[/bold]",
        border_style="yellow",
        box=box.HEAVY,
    ))

def message(text, style="white"):
    console.print(f"[{style}]{text}[/{style}]")

def status_panel(player):
    table = Table(box=box.SIMPLE_HEAVY, title="Status", title_style="bold cyan")
    table.add_column("Stat", style="bold")
    table.add_column("Value", justify="right")
    table.add_row("Name", player.name)
    table.add_row("HP", f"{player.hp}/{player.max_hp}")
    table.add_row("Gold", str(player.gold))
    inv = ", ".join(i.name for i in player.inventory) or "(empty)"
    table.add_row("Inventory", inv)
    console.print(table)

def room_panel(room):
    tag = []
    if room.is_exit: tag.append("[bold green]Exit[/bold green]")
    if room.has_key: tag.append("[yellow]Key[/yellow]")
    tag_line = f"\n[dim]{' • '.join(tag)}[/dim]" if tag else ""
    console.print(Panel(
        f"[bold cyan]{room.name}[/bold cyan]\n{room.description}{tag_line}",
        title="Location",
        border_style="blue",
        box=box.ROUNDED,
    ))

def exits_panel(room):
    ex = ", ".join(f"[bold]{d}[/bold]" for d in room.exits.keys()) or "(none)"
    console.print(Panel.fit(f"Exits: {ex}", border_style="white"))

def inventory_table(items):
    table = Table(title="Inventory", title_style="bold yellow", box=box.SIMPLE)
    table.add_column("Item", style="yellow")
    table.add_column("Effect", style="green")
    for it in items:
        table.add_row(it.name, it.effect)
    console.print(table) 