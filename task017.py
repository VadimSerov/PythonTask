#геометрия 

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
        return ((self.points[0].coord[1]-self.points[0].coord[0])**2+(self.points[1].coord[1]-self.points[1].coord[0])**2)**0.5
        
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
        return self.aSide().length()+self.bSide().length()+self.cSide().length()

    def square(self):
        return (0.5*self.perimeter()*(0.5*self.perimeter()-self.aSide().length())*(0.5*self.perimeter()-self.bSide().length())*(0.5*self.perimeter()-self.cSide().length()))**0.5

#
if __name__ == '__main__' :
    a = Point(0,3)
    b = Point(4,0)
    l1 = Line(a,b)
    c = Point(0,0)
    t1 = Triangle(a,b,c)
#задание 1
    print(repr(a))
    print(repr(b))    
    print(repr(c))
    print(repr(l1))
    print(repr(t1))
#задание 2
    print((a.coord[0],a.coord[1]))
    print((b.coord[0],b.coord[1]))
    print((c.coord[0],c.coord[1]))
    print(l1.length())
    print(t1.aSide().length())
    print(t1.bSide().length())
    print(t1.cSide().length())
    print(t1.perimeter())
    print(t1.square())
    print(a)
    print(b)    
    print(repr(c))
    print(l1)
    print(t1)
