from enum import Enum, auto

from _pyprocgen.block import Block


class Climate(Enum):
    HOT_DESERT = auto()
    ICE_DESERT = auto()
    SEA = auto()

    # Not using Self because for now MyPy does not like Self with Enum's classmethods:
    # see https://github.com/python/mypy/issues/15223.
    @classmethod
    def from_temperature_and_humidity(
        cls,
        temperature: float,
        humidity: float,
    ) -> "Climate":
        """Choose a climate from the temperature and the humidity.

        Args:
            temperature: in Celsius, usually between -80 and +60.
            humidity: in percent.
        """
        del temperature, humidity
        return cls.SEA  # todo

    def get_block(self) -> Block:
        """Get the block of this climate."""
        return Block.WATER  # todo
