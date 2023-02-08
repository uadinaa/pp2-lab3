class Shape:
    def __init__(self, area = ''):
        self.area = area

    def calculate_area(self):
        print(self.area)

p1 = Shape()

class Rectangle(Shape):
    def __init__(self):
        Shape.__init__(self)

class Rectangle(Shape): 
    def __init__(self, width, length): 
        self.width = width 
        self.length = length 
     
    def calculate_area(self): 
        print(self.width * self.length) 
 
p2 = Rectangle(3,4) 
p2.width = int(input())
p2.length = int(input())
p2.calculate_area()
