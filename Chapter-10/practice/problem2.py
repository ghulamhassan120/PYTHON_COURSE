class Calculator:
    def __init__(self,n):
        self.n=n
    def sqaure(self):
        print(f"The sqaure is {self.n*self.n}")
    def cube(self):
        print(f"The sqaure is {self.n*self.n*self.n}")
    def sqaureRoot(self):
        print(f"The sqaure is {self.n**1/2}")

a=Calculator(4)
a.sqaure()
a.cube()
a.sqaureRoot()