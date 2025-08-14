import random
from ui import message
from entities import Enemy

def encounter_enemy(player):
    enemy = Enemy("Goblin", hp=8, damage=3)
    message(f"A wild {enemy.name} appears!", "red")
    while enemy.hp > 0 and player.hp > 0:
        action = input("(A)ttack or (R)un: ").strip().lower()
        if action == "a":
            damage = random.randint(1, 6)
            enemy.hp -= damage
            message(f"You hit the {enemy.name} for {damage} damage.", "green")
            if enemy.hp > 0:
                player.hp -= enemy.damage
                message(f"The {enemy.name} hits you for {enemy.damage} damage!", "red")
        elif action == "r":
            message("You run away!", "yellow")
            return
    if player.hp <= 0:
        message("You were defeated...", "red")
    else:
        player.gold += 5
        message("You defeated the enemy and found 5 gold!", "green")

def find_treasure(player):
    gold_found = random.randint(5, 15)
    player.gold += gold_found
    message(f"You found {gold_found} gold!", "green")

def random_event(player):
    roll = random.randint(1, 3)
    if roll == 1:
        encounter_enemy(player)
    elif roll == 2:
        find_treasure(player)
    else:
        message("The room is eerily quiet...", "cyan")
import random
from ui import message
from entities import Enemy

def encounter_enemy(player):
    enemy = Enemy("Goblin", hp=8, damage=3)
    message(f"A wild {enemy.name} appears!", "red")
    while enemy.hp > 0 and player.hp > 0:
        action = input("(A)ttack or (R)un: ").strip().lower()
        if action == "a":
            damage = random.randint(1, 6)
            enemy.hp -= damage
            message(f"You hit the {enemy.name} for {damage} damage.", "green")
            if enemy.hp > 0:
                player.hp -= enemy.damage
                message(f"The {enemy.name} hits you for {enemy.damage} damage!", "red")
        elif action == "r":
            message("You run away!", "yellow")
            return
    if player.hp <= 0:
        message("You were defeated...", "red")
    else:
        player.gold += 5
        message("You defeated the enemy and found 5 gold!", "green")

def find_treasure(player):
    gold_found = random.randint(5, 15)
    player.gold += gold_found
    message(f"You found {gold_found} gold!", "green")

def random_event(player):
    roll = random.randint(1, 3)
    if roll == 1:
        encounter_enemy(player)
    elif roll == 2:
        find_treasure(player)
    else:
        message("The room is eerily quiet...", "cyan")
