class Student:
    def __init__(self, name, initial_marks):
        self.name = name
        self._marks = initial_marks  

    def get_marks(self):
        """Method to retrieve marks (read-only access)."""
        return self._marks

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100: 
            self._marks = new_marks
            print(f"Marks updated to {self._marks} for {self.name}.")
        else:
            print("Error: Marks must be between 0 and 100.")

student1 = Student("Alice", 75)
print(f"{student1.name}'s initial marks: {student1.get_marks()}")

student1.update_marks(85)
print(f"{student1.name}'s updated marks: {student1.get_marks()}")

