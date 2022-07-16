PI = 3.141592653589793238462643

class Point:
    def __init__(self, x: float, y: float):
        self.coord = (x, y)

    def __repr__(self):
        return "Point(%s, %s)" % self.coord


class Line:
    def __init__(self, point1: Point, point2: Point):
        self.points = (point1, point2)

    def __repr__(self):
        return "Line(%s, %s)" % self.points

    def length(self):
	...
        return ...


class Triangle:
    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.points = (point1, point2, point3)

    def __repr__(self):
        return "Triangle(%s, %s, %s)" % self.points

    def aSide(self):
        return Line(self.points[0], self.points[1])

    def bSide(self):
        return Line(self.points[1], self.points[2])

    def cSide(self):
        return Line(self.points[0], self.points[2])

    def perimeter(self):
        ...
        return ...

    def square(self):
        ...
        return ...
