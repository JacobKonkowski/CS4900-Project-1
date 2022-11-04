from main.classes.Circle import Circle


def test_init():
    circle = Circle((0, 1), 5)
    assert isinstance(circle, Circle)


def test_getters():
    circle = Circle((0, 1), 5)
    assert [circle.get_cord(), circle.get_radius()] == [(0, 1), 5]


def test_setters():
    circle = Circle((0, 1), 5)
    circle.set_cord((3, 2))
    circle.set_radius(10)
    assert [circle.get_cord(), circle.get_radius()] == [(3, 2), 10]