import random
from entities import Enemy
from items import MASTER_KEY
from ui import message

def combat(player, enemy: Enemy):
    message(f"A [red]{enemy.name}[/red] attacks!", "red")
    while enemy.hp > 0 and player.hp > 0:
        choice = input("(A)ttack, (U)se potion, or (R)un: ").strip().lower()
        if choice in ("a", "attack"):
            dmg = random.randint(2, 6)
            enemy.hp -= dmg
            message(f"You strike for {dmg} damage. ({max(enemy.hp,0)} HP left)", "green")
            if enemy.hp <= 0:
                gold = random.randint(4, 9)
                player.gold += gold
                message(f"The {enemy.name} falls. You loot {gold} gold.", "yellow")
                break
            player.hp -= enemy.damage
            message(f"The {enemy.name} hits you for {enemy.damage}. (HP {player.hp})", "red")
        elif choice in ("u", "use"):
            pot = next((i for i in player.inventory if i.name.lower() == "healing potion"), None)
            if not pot:
                message("You have no healing potion.", "yellow")
            else:
                player.hp = min(player.max_hp, player.hp + 5)
                player.inventory.remove(pot)
                message("You drink a healing potion. (+5 HP)", "green")
        elif choice in ("r", "run"):
            if random.random() < 0.5:
                message("You slip away into the shadows...", "cyan")
                return
            else:
                message("You stumble—no escape this time!", "red")
                player.hp -= max(1, enemy.damage - 1)
        else:
            message("You hesitate...", "dim")
    if player.hp <= 0:
        message("You collapse to the cold stone. Darkness closes in...", "red")

def ambient_or_enemy(player, room_name: str):
    """Small random flavor or a simple foe."""
    roll = random.random()
    if roll < 0.5:
        lines = {
            "Dungeon Cell": "Water drips steadily. Somewhere far away, chains rattle.",
            "Hallway": "A cold breeze brushes your neck. The torches crackle.",
            "Guard Room": "Cards flutter on the floor as if moved by a whisper.",
            "Warden's Keep": "The air hums—like a breath held too long.",
            "Exit Gate": "Fresh air seeps in through tiny cracks."
        }
        message(lines.get(room_name, "Silence presses against your ears."), "cyan")
    else:
        foe = random.choice([
            Enemy("Rat", hp=6, damage=2),
            Enemy("Goblin", hp=10, damage=3),
            Enemy("Bone Crawler", hp=8, damage=3),
        ])
        combat(player, foe)

def scripted_room_events(player, room):
    """
    Deterministic story beats tied to rooms.
    Returns a bool indicating whether the game should end (win/lose).
    """
    if not room.visited:
        message(room.story, "white")
        room.visited = True

    if room.name == "Hallway" and not player.saw_shadow:
        message("A shadow darts past at the far end. You freeze.", "magenta")
        player.saw_shadow = True
        return False

    if room.has_key and not player.has_master_key:
        message("A small key rests on the table beside the scattered cards.", "yellow")
        take = input("Take the Master Key? (y/n): ").strip().lower()
        if take in ("y", "yes"):
            player.inventory.append(MASTER_KEY)
            player.has_master_key = True
            message("You pocket the [yellow]Master Key[/yellow].", "green")
        else:
            message("You leave the key where it lies.", "dim")
        return False

    if room.name == "Warden's Keep":
        message("A towering figure steps from the gloom—the Warden.", "red")
        combat(player, Enemy("Warden", hp=16, damage=4))
        return player.hp <= 0  

    if room.is_exit:
        if player.has_master_key:
            message("[bold green]You fit the Master Key. The gate grinds open—fresh air! You escape![/bold green]", "green")
            return True  
        else:
            message("The gate is locked tight. A small keyhole gleams mockingly.", "yellow")
            return False

    ambient_or_enemy(player, room.name)
    return player.hp <= 0
