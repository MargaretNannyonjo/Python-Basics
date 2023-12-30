class Employee:
    def __init__(self, name, Id, position, salary):
        self.name = name
        self.Id = Id
        self.position = position
        self.salary = salary
employee_details = Employee("Ryan", "102435", "Secretary",800000)
print("Name:", employee_details.name)
print("Id:", employee_details.Id)
print("Position:", employee_details.position)
print("Salary:", employee_details.salary)

bonuses = ((10 / 100) * employee_details.salary) + employee_details.salary
updatedSalary = bonuses
print(f"Updated Salary: {updatedSalary}")

