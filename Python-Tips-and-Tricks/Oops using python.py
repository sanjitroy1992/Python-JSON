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

