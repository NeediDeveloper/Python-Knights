class Employee:
    company_name ="Needi Developer"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

print(Employee.company_name)
Employee.change_company_name("AuraOfSurety")
print(Employee.company_name)
Employee.change_company_name("Star link")
print(Employee.company_name)

class MathHelper:
    @staticmethod
    def add_numbers(a, b):
        return a + b

result = MathHelper.add_numbers(5, 10)
print(result)