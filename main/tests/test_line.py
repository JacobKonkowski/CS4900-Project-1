from main.classes.Line import Line


def test_init():
    line = Line((0, 1), (1, 0))
    assert isinstance(line, Line)


def test_getters():
    line = Line((10, 3), (7, 2))
    assert [line.get_cord1(), line.get_cord2()] == [(10, 3), (7, 2)]


def test_setters():
    line = Line((10, 3), (7, 2))
    line.set_cord1((0, 1))
    line.set_cord2((1, 0))
    assert [line.get_cord1(), line.get_cord2()] == [(0, 1), (1, 0)]
