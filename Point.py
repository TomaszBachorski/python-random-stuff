class Point:
    x=0
    y=0
    def __init__(self, __x, __y):
        self.x == __x
        self.y == __y
        
    def print(self):
        # Showing information about our object
        # sep="" - changing separator instead of deafult space
        print("Point(", self.getX() ,", ", self.getY(), ")\n", sep="")

    def setX(self, x):
        self.x=x

    def setY(self, y):
        self.y=y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def saveToFile(self, file_path):
        f = open(file_path, "w")
        f.write("Point("+ str(self.getX()) +", "+ str(self.getY())+ ")\n")
        f.close()