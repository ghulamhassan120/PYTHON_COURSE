class Employee:
    a=1
    @classmethod
    def show(self):
        print(f"The class value of a is {self.a}")
    @property
    def name(self):
        return self.ename
    @name.setter
    def name(self,value):
        self.ename = value
e=Employee()
e.a=45
e.name="Hassan Khan"
print(e.ename)
e.show()