class Circle:
    def __init__(self, cord, radius):
        self._cord = cord
        self._radius = radius

    def get_cord(self):
        # center of circle
        return self._cord

    def get_radius(self):
        return self._radius

    def set_cord(self, cord):
        self._cord = cord

    def set_radius(self, radius):
        self._radius = radius