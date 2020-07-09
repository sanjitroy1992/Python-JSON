"""
What is Polymorphism : The word polymorphism means having many forms. In programming, polymorphism means same
function name (but different signatures) being uses for different types.
"""
#1. Python program to demonstrate in-built poly- morphic functions

# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))

#2. Examples of used defined polymorphic functions :
# A simple Python function to demonstrate
# Polymorphism

def add(x, y, z = 0):
	return x + y+z

# Driver code
print(add(2, 3))
print(add(2, 3, 4))



"""
3. Polymorphism with class methods:
Below code shows how python can use two different class types, in the same way. We create a for loop that iterates 
through a tuple of objects. Then call the methods without being concerned about which class type each object is. 
We assume that these methods actually exist in each class.
"""
class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()


"""
4. Method Overriding
In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in 
the parent class. In inheritance, the child class inherits the methods from the parent class. 
However, it is possible to modify a method in a child class that it has inherited from the parent class. 
This is particularly useful in cases where the method inherited from the parent class dose not quite fit the child class. 
In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child 
class is known as Method Overriding.
"""


class Bird:

    def intro(self):
        print("There are many types of birds.")


    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

