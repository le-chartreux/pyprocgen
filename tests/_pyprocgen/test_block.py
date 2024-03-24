from _pyprocgen.block import Block


def test___eq__() -> None:
    block1 = Block.ROCK
    block2 = Block.ROCK
    assert block1 is block2
    block2 = Block.AIR
    assert block1 is not block2
