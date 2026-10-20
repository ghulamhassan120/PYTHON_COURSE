class Employee:
    a=1
class Programmer(Employee):
    b=2
class Managers(Programmer):
    c=3

o=Managers()
print(o.a)
print(o.b)
print(o.c)