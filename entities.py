from dataclasses import dataclass, field
from typing import List

@dataclass
class Item:
    name: str
    effect: str 

@dataclass
class Player:
    name: str
    max_hp: int = 20
    hp: int = 20
    gold: int = 0
    inventory: List[Item] = field(default_factory=list)
    saw_shadow: bool = False
    has_master_key: bool = False

@dataclass
class Enemy:
    name: str
    hp: int
    damage: int
