from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Room:
    name: str
    description: str
    story: str
    exits: Dict[str, int]   
    has_key: bool = False
    is_exit: bool = False
    visited: bool = False

def generate_world():
    """
    Static, hand-crafted mini-map with a story path:
      0: Dungeon Cell  -> north -> 1 Hallway
      1: Hallway       -> east  -> 2 Guard Room
      2: Guard Room    -> north -> 3 Warden's Keep
      3: Warden's Keep -> east  -> 4 Exit Gate (locked without Master Key)
    """
    rooms = [
        Room(
            name="Dungeon Cell",
            description="A cold, damp cell with rusty bars.",
            story="Chains clink as you rise. The corridor beyond is quiet—for now.",
            exits={"north": 1},
        ),
        Room(
            name="Hallway",
            description="A narrow corridor lit by flickering torches.",
            story="Your footsteps echo. A shadow darts at the far end, vanishing.",
            exits={"south": 0, "east": 2},
        ),
        Room(
            name="Guard Room",
            description="Upturned stools and scattered cards litter the floor.",
            story="Whoever was here left in a hurry. A glint catches your eye on a table.",
            exits={"west": 1, "north": 3},
            has_key=True,
        ),
        Room(
            name="Warden's Keep",
            description="Broken armor lines the walls. The air feels heavy.",
            story="You sense a presence watching—judging.",
            exits={"south": 2, "east": 4},
        ),
        Room(
            name="Exit Gate",
            description="A heavy iron gate leading to the surface.",
            story="Beyond the bars you smell fresh air. Freedom is close.",
            exits={"west": 3},
            is_exit=True,
        ),
    ]
    return rooms
