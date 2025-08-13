class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

items_library = [
    Item("Health Potion", "+20 HP"),
    Item("Sword", "+5 Attack"),
    Item("Shield", "-5 Damage Taken"),
]