from main.classes.Line import Line
from main.classes.Point import Point
from main.classes.Circle import Circle


class EuclideanSpace:

    def __init__(self, geometric_obj):
        # geo obj of a point, line segment, or circle
        self._objects_in_space = {'points': [], 'lines': [], 'circles': []}
        self._geometric_obj = geometric_obj

    def set_geo_object(self, geometric_obj):
        # for addition or removal
        self._geometric_obj = geometric_obj

    def get_geo_object(self):
        # return current object
        return self._geometric_obj

    def get_objects_in_space(self):
        # returns a list of current objects in space
        return self._objects_in_space

    def add_geo_object(self):
        # adds a current set geo obj to the space
        if isinstance(self._geometric_obj, Line):
            self._objects_in_space["lines"].append(self._geometric_obj)
        elif isinstance(self._geometric_obj, Point):
            self._objects_in_space["points"].append(self._geometric_obj)
        elif isinstance(self._geometric_obj, Circle):
            self._objects_in_space["circles"].append(self._geometric_obj)

    def remove_geo_object(self):
        # removes current set geo obj in the space
        if isinstance(self._geometric_obj, Line):
            self._objects_in_space["lines"].remove(self._geometric_obj)
        elif isinstance(self._geometric_obj, Point):
            self._objects_in_space["points"].remove(self._geometric_obj)
        elif isinstance(self._geometric_obj, Circle):
            self._objects_in_space["circles"].remove(self._geometric_obj)
