from enum import Enum, auto


class Block(Enum):
    """Atomic piece of the world."""

    ROCK = auto()
    AIR = auto()
    DIRT = auto()
    WATER = auto()
