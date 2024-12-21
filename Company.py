class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}, Position: {self.position}, Salary: {self.salary} UAH"


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def total_salary(self):
        return sum(emp.salary for emp in self.employees)

    def show_employees(self):
        for emp in self.employees:
            print(emp)

# Приклад використання:
dept = Department("IT Department")
emp1 = Employee("Alice", "Developer", 15000)
emp2 = Employee("Bob", "Manager", 20000)

dept.add_employee(emp1)
dept.add_employee(emp2)

dept.show_employees()
print("Total Salary:", dept.total_salary())
