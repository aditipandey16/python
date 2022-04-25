class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(self.num**2)
    def squareroot(self):
        print(self.num**1/2)
    def cube(self):
        print(self.num**3)
a= Calculator(3)
a.square()
a.cube()
a.squareroot()
    
    
        