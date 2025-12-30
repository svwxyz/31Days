class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    def display_details(self):
        print(f"The Name of Employee is {self.name} with id {self.id} and salary {self.salary}")

    def annual_salary(self):
        print(f"Annual Salary for {self.name} would be {self.salary*12}")


emp1 = Employee(1,"sumit vishwakarma",90000)
emp2 = Employee(2,"Pooja",98000)

emp1.display_details()
emp2.display_details()

emp1.annual_salary()
emp2.annual_salary()