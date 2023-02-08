class Point():
    def __init__(self, d = '', a = ''):
        self.d = d
        self.a = a

    def Show(self):
        print(self.d , self.a)

    def Move(self):
        print(self.d + 3 , self.a + 5)

    def Dist(self):
        print (((self.d**2) + (self.a**2))**(1/2)) 

p1 = Point()
p1.d = int(input())
p1.a = int(input())

p1.Show()
p1.Move()
p1.Dist()
