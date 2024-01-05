# Object-oriented programming

# Classes and objects
# Constructors
# Inheritance
# Multiple inheritance

# Class is a blueprint for an object.
# Object is an instance of a class.

# Sample class 1

class Variable:
    x = 5

Object1 = Variable()
print(Object1.x)

# Sample class 2

# All classes have a function called __init__(), which is always executed when the class is being initiated.

class Person:
     def __init__(self,name,age):
         self.name=name
         self.age=age
         print("Hello",self.name,".You are",self.age ,"years old . ")

Person1 = Person("Nehanth",20)

# The __init__() function is called automatically every time the class is being used to create a new object.

# The __str__() function controls what should be returned when the class object is represented as a string.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

Person1 = Person("Nehanth", 20)
print(Person1)

# Objects can also contain methods. Methods in objects are functions that belong to the object.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Nehanth", 36)
p1.myfunc()