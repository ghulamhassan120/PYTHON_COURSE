class Employee:
    company = "Google" ,
    salary=120000,
    def __init__(self,name,sarlry,company):
        self.company=company,
        self.name=name,
        self.sarlry=sarlry
        print("dunder method")
    def GetInfo(self):
        print(f"Sarlay {self.salary} Company : {self.company}")
    @staticmethod
    def greet():
        print("Good morning")


harry = Employee("Hassan",1200000,"Google") 
print(harry.name,harry.sarlry)