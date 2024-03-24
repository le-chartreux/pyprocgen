import pytest
from perlin_noise import PerlinNoise

from _pyprocgen.block import Block
from _pyprocgen.world import World


def test___init__() -> None:
    altitude_noise = PerlinNoise()
    temperature_noise = PerlinNoise()
    humidity_noise = PerlinNoise()
    _ = World(altitude_noise, temperature_noise, humidity_noise)


def test_get_block(world: World) -> None:
    assert world.get_block(0, 0) == Block.AIR


@pytest.fixture()
def world() -> World:
    altitude_noise = PerlinNoise()
    temperature_noise = PerlinNoise()
    humidity_noise = PerlinNoise()
    return World(altitude_noise, temperature_noise, humidity_noise)
