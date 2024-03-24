from perlin_noise import PerlinNoise

from _pyprocgen.block import Block


class World:
    """Set of blocks determined by altitude, temperature and humidity."""

    def __init__(
        self,
        altitude_noise: PerlinNoise,
        temperature_noise: PerlinNoise,
        humidity_noise: PerlinNoise,
    ) -> None:
        self._altitude_noise = altitude_noise
        self._temperature_noise = temperature_noise
        self._humidity_noise = humidity_noise

    def get_block(self, x: int, y: int) -> Block:
        altitude = self._altitude_noise([x, y])
        temperature = self._temperature_noise([x, y])
        humidity = self._humidity_noise([x, y])
        del altitude, temperature, humidity
        return Block.AIR  # todo
