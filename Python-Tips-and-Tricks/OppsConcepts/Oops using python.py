# Inheritance
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



"""
Duck Typing
"""
# class TheHobbit:
#     def __len__(self):
#        return 95022
#
# the_hobbit = TheHobbit()
#
# len(the_hobbit)
#
# my_str = "Hello World"
# my_list = [34, 54, 65, 78]
# my_dict = {"one": 123, "two": 456, "three": 789}
#
# len(my_str)
# len(my_list)
# len(my_dict)
# len(the_hobbit)
# my_int = 7
# my_float = 42.3
#
# len(my_int)
# len(my_float)

# Example 2
class duck:
    def quack(self):
        print("Quack, Quack")
    def fly(self):
        print("Flap, Flap")

class person:
    def quack(self):
        print("I am quacking like a duck")
    def fly(self):
        print("I am flapping my arms")

def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
    except:
        print("it dose not have same behavior as a duck")

d = duck()
quack_and_fly(d)

p = person()
quack_and_fly(p)

