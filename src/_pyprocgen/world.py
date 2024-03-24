from typing import Self

from perlin_noise import PerlinNoise

from _pyprocgen.block import Block


class World:
    """Set of blocks determined by temperature and humidity."""

    def __init__(
        self,
        temperature_noise: PerlinNoise,
        humidity_noise: PerlinNoise,
    ) -> None:
        self._temperature_noise = temperature_noise
        self._humidity_noise = humidity_noise

    def get_block_from_coordinates(self, x: int, y: int) -> Block:
        temperature = self._get_temperature(x, y)
        humidity = self._get_humidity(x, y)
        return Block.from_climate(temperature, humidity)

    def _get_temperature(self, x: int, y: int) -> float:
        """Compute temperature in Celsius."""
        temperature_as_noise: float = self._temperature_noise((x, y))
        return temperature_as_noise * 40 + 15

    def _get_humidity(self, x: int, y: int) -> float:
        """Compute the percentage of humidity."""
        humidity_as_noise: float = self._humidity_noise((x, y))
        humidity_as_noise_between_zero_and_one = (humidity_as_noise + 1) / 2
        return humidity_as_noise_between_zero_and_one * 100

    @classmethod
    def from_seed(cls, seed: int) -> Self:
        return cls(PerlinNoise(seed=seed), PerlinNoise(seed=seed + 1500))
