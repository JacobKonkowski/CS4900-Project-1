import pytest
from main.classes.Point import Point


def test_init():
    point = Point((0, 1))
    assert isinstance(point, Point)


def test_getters():
    point = Point((0, 1))
    assert point.get_cord() == (0, 1)


def test_setters():
    point = Point((0, 1))
    point.set_cord((1, 0))
    assert point.get_cord() == (1, 0)

