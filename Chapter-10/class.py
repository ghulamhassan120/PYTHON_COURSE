class Employee:
    company = "Google" # Specific to Each Class
harry = Employee() # Object Instantiation
harry.company
Employee.company = "YouTube" # Changing Class Attribute
print(harry.company)