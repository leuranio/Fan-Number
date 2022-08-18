from pytest import fixture

from game.level import Level


@fixture
def level():
    return Level()
