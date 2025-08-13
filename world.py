class Room:
    def __init__(self, description, enemy=None, item=None):
        self.description = description
        self.enemy = enemy
        self.item = item

world_map = {
    "entrance": Room("You stand at the dungeon entrance."),
    "hall": Room("A dark hallway with dripping water."),
    "treasure": Room("A room glittering with treasure."),
    "boss": Room("A large ominous chamber... the boss awaits."),
}

connections = {
    "entrance": ["hall"],
    "hall": ["entrance", "treasure", "boss"],
    "treasure": ["hall"],
    "boss": ["hall"],
}