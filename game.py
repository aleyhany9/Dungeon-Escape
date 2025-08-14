from ui import banner, status_panel, room_description, message, inventory_table
from entities import Player
from items import get_starting_items
from world import generate_world
from events import random_event

def main():
    banner()
    name = input("Enter your name: ")
    player = Player(name)
    player.inventory.extend(get_starting_items())

    rooms = generate_world()
    current_room = 0

    while True:
        status_panel(player)
        room_description(rooms[current_room])
        
        if rooms[current_room].name == "Treasure Room":
            message("You see piles of gold around you!", "yellow")
        
        if rooms[current_room].name == "Exit Gate":
            message("You escaped the dungeon! 🎉", "green")
            break

        command = input("Command (move [dir] / inv / event / quit): ").strip().lower()

        if command.startswith("move"):
            parts = command.split(maxsplit=1)
            if len(parts) < 2:
                message("Please specify a direction! Example: move north", "red")
                continue
            _, direction = parts
            if direction in rooms[current_room].exits:
                current_room = rooms[current_room].exits[direction]
            else:
                message("You can't go that way.", "red")

        
        elif command == "inv":
            inventory_table(player.inventory)
        
        elif command == "event":
            random_event(player)

        elif command == "quit":
            message("Thanks for playing!", "cyan")
            break

if __name__ == "__main__":
    main()
