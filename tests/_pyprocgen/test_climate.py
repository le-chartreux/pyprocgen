from _pyprocgen.climate import Climate


def test___eq__() -> None:
    climate1 = Climate.HOT_DESERT
    climate2 = Climate.HOT_DESERT
    assert climate1 == climate2


def test___eq___not_equal() -> None:
    climate1 = Climate.HOT_DESERT
    climate2 = Climate.SEA
    assert climate1 != climate2


def test_from_temperature_and_humidity() -> None:
    assert Climate.from_temperature_and_humidity(10, 100) == Climate.SEA
