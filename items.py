from entities import Item

def get_starting_items():
    return [
        Item("Healing Potion", "+5 HP"),
        Item("Dagger", "+2 ATK"),
    ]

MASTER_KEY = Item("Master Key", "story:key")
