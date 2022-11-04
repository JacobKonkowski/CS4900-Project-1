from main.classes.Euclidean_Space import EuclideanSpace
from main.classes.Line import Line
from main.classes.Point import Point
from main.classes.Circle import Circle


def test_init():
    line = Line((0, 1), (1, 0))
    space = EuclideanSpace(line)
    assert isinstance(space, EuclideanSpace)


def test_getter():
    line = Line((0, 1), (1, 0))
    space = EuclideanSpace(line)
    assert isinstance(space.get_geo_object(), Line)


def test_setter():
    line = Line((0, 1), (1, 0))
    space = EuclideanSpace(line)

    line2 = Line((2, 5), (5, 2))
    space.set_geo_object(line2)
    assert isinstance(space.get_geo_object(), Line)


def test_get_objects_in_space():
    line = Line((0, 1), (1, 0))
    space = EuclideanSpace(line)
    assert len(space.get_objects_in_space()["lines"]) == 0


def test_add_geo_object_point():
    point = Point((5, 6))
    space = EuclideanSpace(point)

    space.add_geo_object()
    x = space.get_objects_in_space()
    print(x)
    assert len(x["points"]) > 0


def test_add_geo_object_line():
    line = Line((0, 1), (1, 0))
    space = EuclideanSpace(line)

    space.add_geo_object()
    x = space.get_objects_in_space()
    print(x)
    assert len(x["lines"]) > 0


def test_add_geo_object_circle():
    circle = Circle((0, 1), 3)
    space = EuclideanSpace(circle)

    space.add_geo_object()
    x = space.get_objects_in_space()
    print(x)
    assert len(x["circles"]) > 0


def test_remove_geo_object_point():
    point = Point((6, 2))
    space = EuclideanSpace(point)

    space.add_geo_object()
    x = space.get_objects_in_space()
    length = len(x["points"])

    space.remove_geo_object()

    assert len(space.get_objects_in_space()["points"]) < length


def test_remove_geo_object_line():
    line = Line((0, 1), (1, 0))
    space = EuclideanSpace(line)

    space.add_geo_object()
    x = space.get_objects_in_space()
    length = len(x["lines"])

    space.remove_geo_object()

    assert len(space.get_objects_in_space()["lines"]) < length


def test_remove_geo_object_circle():
    circle = Circle((0, 1), 3)
    space = EuclideanSpace(circle)

    space.add_geo_object()
    x = space.get_objects_in_space()
    length = len(x["circles"])

    space.remove_geo_object()

    assert len(space.get_objects_in_space()["circles"]) < length
