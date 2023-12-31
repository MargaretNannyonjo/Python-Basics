class Person:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


class Employee(Person):
    def __init__(self, salary, emp_id):  # Include emp_id in the constructor
        super().__init__(salary)
        self.__Id = emp_id  # Set the employee ID here

    def get_Id(self):
        return self.__Id

    def employee_salary(self):
        return self.get_salary()


class Manager(Employee):
    def manager_Id(self):
        return self.get_Id()

