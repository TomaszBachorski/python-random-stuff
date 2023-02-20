from Point import Point
class Polygon():
    points = []
    size = 0

    def __init__(self, __points, __size):
        self.points = __points
        self.points = []
        for i in range(__size):
            self.points.append(Point(__points[i].getX() , __points[i].getY()))

    def print(self):
        for i in range(self.size):
            print("(" + str(self.points[i].getX()), str(self.points[i].getY()) +")", sep=", ")