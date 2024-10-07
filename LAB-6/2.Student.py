class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        
student1 = Student('John','2')   

print(f"Name:{student1.name},Age:{student1.roll_no}")
