from ui import banner, blurb_and_intro, status_panel, room_panel, exits_panel, inventory_table, message
from entities import Player
from items import get_starting_items
from world import generate_world
from events import scripted_room_events

def normalize(cmd: str):
    return cmd.strip().lower()

def main():
    banner()
    blurb_and_intro()

    name = input("Enter your name: ").strip() or "Prisoner"
    player = Player(name=name)
    player.inventory.extend(get_starting_items())

    rooms = generate_world()
    current = 0  

    while True:
        status_panel(player)
        room = rooms[current]
        room_panel(room)
        exits_panel(room)

        end_now = scripted_room_events(player, room)
        if end_now:
            
            break
        if player.hp <= 0:
            break

        cmd = normalize(input("Command (move [dir] / look / inv / use [potion] / help / quit): "))
        if not cmd:
            continue

        if cmd in ("quit", "q", "exit"):
            message("Thanks for playing!", "cyan")
            break

        if cmd in ("help", "h", "?"):
            message(
                "Commands: move [north|south|east|west], look, inv, use potion, quit",
                "cyan",
            )
            continue

        if cmd.startswith("use"):
            parts = cmd.split(maxsplit=1)
            if len(parts) < 2:
                message("Use what? Try: use potion", "yellow")
                continue
            item_name = parts[1].strip().lower()
            if item_name in ("potion", "healing potion"):
                idx = next((i for i, it in enumerate(player.inventory) if it.name.lower() == "healing potion"), None)
                if idx is None:
                    message("You don't have a healing potion.", "yellow")
                else:
                    player.hp = min(player.max_hp, player.hp + 5)
                    player.inventory.pop(idx)
                    message("You drink a healing potion. (+5 HP)", "green")
            else:
                message("You can't use that right now.", "yellow")
            continue

        if cmd == "inv":
            inventory_table(player.inventory)
            continue

        if cmd == "look":
            room_panel(room)
            exits_panel(room)
            continue

        if cmd.startswith("move"):
            parts = cmd.split(maxsplit=1)
            if len(parts) < 2:
                message("Please specify a direction. Example: move north", "yellow")
                continue
            direction = parts[1].strip().lower()
            if direction in room.exits:
                current = room.exits[direction]
            else:
                message("You can't go that way.", "red")
            continue

        message("Unknown command. Type 'help' for options.", "yellow")

if __name__ == "__main__":
    main()     