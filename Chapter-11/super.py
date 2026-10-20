class Employee:
    def __init__(self):
        print("Costructor in Employee")
    a=1
class Programmer(Employee):
    def __init__(self):
            
            print("Costructor in Programmer")
    b=2
class Managers(Programmer):
    def __init__(self):
            super().__init__()
            print("Costructor in Managers")
    c=3

o=Managers()
print(o.a)
print(o.b)
print(o.c)