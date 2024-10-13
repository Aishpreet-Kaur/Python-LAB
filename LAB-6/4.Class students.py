class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def info(self):
    print(f"Student name:{self.name} , Student age:{self.age}")

student1 = Student("Khushi",20)
student2 = Student("Aadya",19)

student1.info()
student2.info()
