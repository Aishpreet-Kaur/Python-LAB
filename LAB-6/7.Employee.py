class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name  # Public attribute
        self._emp_id = emp_id  # Protected attribute
        self.__salary = salary  # Private attribute

    def display_details(self):
        print(f"Name: {self.name}, Employee ID: {self._emp_id}, Salary: {self.__get_salary()}")

    def _update_emp_id(self, new_id):
        if isinstance(new_id, int) and new_id > 0:
            self._emp_id = new_id
            print(f"Employee ID updated to: {self._emp_id}")
        else:
            print("Invalid Employee ID! Please provide a positive integer.")

    def __get_salary(self):
        return self.__salary

    def update_salary(self, new_salary):
        if self.__validate_salary(new_salary):
            self.__salary = new_salary
            print(f"Salary updated to: {self.__salary}")
        else:
            print("Invalid salary amount!")

    def __validate_salary(self, salary):
        return salary > 0

emp1 = Employee("John Doe", 101, 50000)

emp1.display_details()
emp1._update_emp_id(102)
emp1.update_salary(60000)
