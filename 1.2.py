class Shape:
    def __init__(self):
        self.area = 0

    def calculate_area(self):
        print(self.area)

p1 = Shape()
p1.calculate_area()

class Square():
    def __init__(self, length = ''):
        self.length = length 

    def calculate_area(self):
        print(self.length * self.length)


p2 = Square()
p2.length = int(input())
p2.calculate_area()
