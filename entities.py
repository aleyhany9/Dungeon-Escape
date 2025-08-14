class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.gold = 0
        self.inventory = []

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
