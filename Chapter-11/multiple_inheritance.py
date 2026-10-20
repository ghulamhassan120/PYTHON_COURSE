# Inheritance & More On OOPS
class Employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class Coder:
    language="python"
    def printLanguage(self):
        print(f"{self.language}")




class Programmer(Employee,Coder):
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is and the salary is {self.language}")


a=Employee()
b=Programmer()
print(a.company)
b.showLanguage()