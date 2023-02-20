from Point import Point

from Polygon import Polygon

p1 = Point(0, 0)
p2 = Point(0, 2)
p3 = Point(2, 2)
p4 = Point(2, 0)

p1.print()
p2.setY(2).print()
p3.setX(2).setY(2).print()
p4.setX(2).print()
points = [p1, p2, p3, p4]

#polygon = Polygon(points, 4)
#polygon.print()
