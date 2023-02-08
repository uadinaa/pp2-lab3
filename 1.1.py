class upline:

    def __init__ (self, myline = ''):
        self.myline = myline 

    def getString(self):
        self.myline = input()

    def printString(self):
        print(self.myline.upper())


p1 = upline()
p1.getString()
p1.printString()

