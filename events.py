import random
from ui import message
from items import items_library
from entities import Enemy

def enemy_encounter(player):
    enemy = Enemy("Goblin", 30, 5)
    message(f"A wild {enemy.name} appears!", "red")
    while enemy.hp > 0 and player.hp > 0:
        action = input("[A]ttack or [R]un: ").lower()
        if action == "a":
            enemy.hp -= player.attack
            player.hp -= enemy.attack
            message(f"You hit the {enemy.name}!", "green")
        elif action == "r":
            message("You escaped!", "yellow")
            return
    if player.hp <= 0:
        message("You died!", "red")

def find_item(player):
    item = random.choice(items_library)
    player.inventory.append(item)
    message(f"You found {item.name}! ({item.effect})", "yellow")