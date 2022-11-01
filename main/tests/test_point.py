import pytest


class TestPoint:

    def test_get_coords(self):
        point = Point()
        assert point.get_coords() == [0,1,2,3,4]

    def test_set_coords(self):
        point = Point([4,3,2,1,0])
        point.set_coords([0,1,2,3,4])

        assert point.get_coords() == [0,1,2,3,4]

    def test_set_coords_type(self):
        with pytest.raises(TypeError):
            point = Point()
            point.set_coords("Donkey")
