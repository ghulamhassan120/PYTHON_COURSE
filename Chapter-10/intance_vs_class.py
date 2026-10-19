class Employee:
    company = "Google" ,
    salary=120000,
    def GetInfo(self):
        print(f"Sarlay {self.salary} Company : {self.company}")
    @staticmethod
    def greet():
        print("Good morning")


harry = Employee() 
harry.GetInfo()
harry.greet()
Employee.GetInfo(harry)
