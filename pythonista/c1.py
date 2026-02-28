import math

class Point:
    
    def __init__(self, intx, inty):
        self.x = intx
        self.y = inty

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def dist_origin(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def dist(self, p2):
        x_diff = p2.getX - self.getX
        y_diff = p2.getY - self.getY
        return math.sqrt(x_diff**2 + y_diff**2)

p = Point(7, 6)
print(p.dist_origin())