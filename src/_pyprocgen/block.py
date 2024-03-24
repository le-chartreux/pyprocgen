from enum import Enum, auto


class Block(Enum):
    """Atomic piece of the world."""

    ROCK = auto()
    AIR = auto()
    DIRT = auto()
    WATER = auto()

    # Not using Self because for now MyPy does not like Self with Enum's classmethods:
    # see https://github.com/python/mypy/issues/15223.
    @classmethod
    def from_climate(cls, temperature: float, humidity: float) -> "Block":
        """Find the block that matches the given climate.

        Args:
            temperature: in Celsius, usually between -80 and +60.
            humidity: in percent.
        """
        del temperature, humidity
        return cls.DIRT  # todo
