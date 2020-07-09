"""
It is the mechanism in which one class is allow to inherit the features(fields and methods) of another class.
Important terminology:

*Super Class: The class whose features are inherited is known as super class(or a base class or a parent class).
*Sub Class: The class that inherits the other class is known as sub class(or a derived class, extended class, or child class).
The subclass can add its own fields and methods in addition to the superclass fields and methods.
*Reusability: Inheritance supports the concept of “reusability”, i.e. when we want to create a new class and there is
already a class that includes some of the code that we want, we can derive our new class from the existing class.
By doing this, we are reusing the fields and methods of the existing class.
"""
"""Types of Inheritance
#1. Single Inheritance:
# Single inheritance enables a derived class to inherit properties from a single parent class,
# thus enabling code reusability and addition of new features to existing code.
"""

# Python program to demonstrate
# single inheritance


# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class
class Child(Parent):
	def func2(self):
		print("This function is in child class.")

# Driver's code
object = Child()
object.func1()
object.func2()

"""2. Multiple Inheritance: When a class can be derived from more than one base classes this type of inheritance is called
# multiple inheritance. In multiple inheritance, all the features of the base classes are inherited into the derived class.
"""

# Python program to demonstrate
# multiple inheritance


# Base class1
class Mother:
	mothername = ""
	def mother(self):
		print(self.mothername)

# Base class2
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)

# Derived class
class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)

# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

"""
Multilevel Inheritance
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. 
This is similar to a relationship representing a child and grandfather.
"""

# Python program to demonstrate
# multilevel inheritance


# Base class
class Grandfather:
	grandfathername =""
	def grandfather(self):
		print(self.grandfathername)

# Intermediate class
class Father(Grandfather):
	fathername = ""
	def father(self):
		print(self.fathername)

# Derived class
class Son(Father):
	def parent(self):
		print("GrandFather :", self.grandfathername)
		print("Father :", self.fathername)

# Driver's code
s1 = Son()
s1.grandfathername = "Srinivas"
s1.fathername = "Ankush"
s1.parent()

"""
4. Inheriting constructors using super class """

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name +"."+ self.last_name + "@gmail.com"
        self.salary = salary

    def give_raise(self, salary_raise):
        self.salary += salary_raise
        return self.salary


class Developer(Employee):
    def __init__(self, first_name, last_name, salary, prog_languages):
        super().__init__(first_name, last_name, salary)
        self.prog_language = prog_languages

    def add_language(self, lang):
        self.prog_language += [lang]


p1 = Employee("Sanjit", "Roy", 1000)
p2 = Developer("Anmol", "Ratan", 1500, ['python', 'java'])
print(p1.first_name)
print(p2.first_name)
p2.add_language('javascript')
p2.give_raise(500)
print(p2.prog_language)
print(p2.salary)