class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

name1 = input("enter a name:")
age1 = int(input("enter a age: "))
person1 = Person(name1,age1)

name2 = input("enter a name:")
age2 = int(input("enter a age: "))
person2 = Person(name2,age2)

print(f"Name:{person1.name},Age:{person1.age}")
print(f"Name:{person2.name},Age:{person2.age}")
