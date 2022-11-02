import pytest


class TestCircle:

    def test_get_coords(self):
        circle = Circle()
        assert circle.get_cords() == [0, 1, 2, 3, 4]

    def test_set_coords(self):
        circle = Circle([4, 3, 2, 1, 0])
        circle.set_coords([0, 1, 2, 3, 4])

        assert circle.get_coords() == [0, 1, 2, 3, 4]

    def test_get_radius(self):
        circle = Circle()
        assert circle.get_radius() == 3

    def test_set_radius(self):
        circle = Circle(1)
        circle.set_radius(3)

        assert circle.get_radius() == 3

    def test_set_coords_type(self):
        with pytest.raises(TypeError):
            circle = Circle()
            circle.set_coords("Donkey")

    def test_set_radius_type(self):
        with pytest.raises(TypeError):
            circle = Circle()
            circle.set_radius("Donkey")
