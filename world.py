import random

class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits  

def generate_world():
    rooms = [
        Room("Dungeon Cell", "A cold, damp cell with rusty bars.", {"north": 1}),
        Room("Hallway", "A narrow hallway lit by flickering torches.", {"south": 0, "east": 2}),
        Room("Armory", "Old weapons line the walls, most are broken.", {"west": 1, "north": 3}),
        Room("Treasure Room", "Glittering gold is piled high!", {"south": 2, "east": 4}),
        Room("Exit Gate", "A heavy iron gate leading to freedom!", {"west": 3}),
    ]
    return rooms
