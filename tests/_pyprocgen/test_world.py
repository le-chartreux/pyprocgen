import pytest
from perlin_noise import PerlinNoise

from _pyprocgen.block import Block
from _pyprocgen.climate import Climate
from _pyprocgen.world import World


def test___init__() -> None:
    temperature_noise = PerlinNoise()
    humidity_noise = PerlinNoise()
    _ = World(temperature_noise, humidity_noise)


def test_get_block_from_coordinates(world: World) -> None:
    assert world.get_block_from_coordinates(0, 0) == Block.WATER


def test_get_climate_from_coordinates(world: World) -> None:
    assert world.get_climate_from_coordinates(0, 0) == Climate.SEA


def test__get_temperature(world: World) -> None:
    assert world._get_temperature(0, 0) == 15


def test__get_humidity(world: World) -> None:
    assert world._get_humidity(0, 0) == 50


def test_from_seed() -> None:
    world1 = World.from_seed(10)
    world2 = World.from_seed(10)
    block1 = world1.get_block_from_coordinates(10, -5)
    block2 = world2.get_block_from_coordinates(10, -5)
    assert block1 == block2


@pytest.fixture()
def world() -> World:
    return World.from_seed(0)
