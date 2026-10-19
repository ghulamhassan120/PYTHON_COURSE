class Programmer:
    company="Microsoft",
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("Hassan",120000,2232)
print(p.name,p.salary,p.pin)