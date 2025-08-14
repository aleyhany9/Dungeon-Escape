class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

def get_starting_items():
    return [
        Item("Healing Potion", "+5 HP"),
        Item("Dagger", "+2 attack")
    ]
