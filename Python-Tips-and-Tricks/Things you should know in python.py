# Swap two values
a = 10
b = 20
a, b = b, a
print(a, b)

# Max and min function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Largest number: {}".format(max(numbers)))
print("Smallest number: {}".format(min(numbers)))

# List comprehension
# find all the even numbers in first 20 numbers
even = [x for x in range(20) if x % 2 == 0]
print("Even numbers: {}".format(even))

# map function:
# square of all the numbers in a list
square = list(map(lambda x : x*x, numbers))
print("Square of all the numbers using map: {}".format(square))

# filter function:
odd = list(filter(lambda x:x%2==1, numbers))
print("Odd numbers using filter: {}".format(odd))

# reduce function:
from functools import reduce
product = reduce(lambda x, y: x*y, numbers)
print("Product of numbers using reduce: {}".format(product))
addition = reduce(lambda x, y: x+y, numbers)
print("Addition of numbers using reduce: {}".format(addition))

# String Formatting
name = "Sanjit"
age = 27
print("My name is {} and age is {}".format(name, age))
hello = f"Hello, {name} i guess your age is {age}"
print(hello)

## String to a list
str1 = "Python"
list1 = list(map(str, str1))
assert list1 == ['P', 'y', 't', 'h', 'o', 'n']
print(list1)

## List to string
list1 = ['P', 'y', 't', 'h', 'o', 'n']
str2 = ''.join(list1)
assert str2 == 'Python'
print(str2)

## given two string, what would be the output for print(str1 == str2)
string1 = 'hello1'
string2 = 'hello2'
print(string1 == string2)

# List Comprehension
square_number = [x*x for x in numbers]
print("Square of numbers : {}".format(square_number))

# List operations
# list can be used as a stack or as a queue
stack = []
stack.append(1)
stack.append(2)

queue = []
queue.append(1)
queue.append(2)

print("Stack pop item: {}".format(stack.pop()))
print("Queue pop item: {}".format(queue.pop(0)))

# Set operations
set1 = set([1, 2, 2, 3, 4, 4])
set2 = set([2,3,4,4,5,6,7])
print("Intersection between two sets using set1.ntersection(set2): {}".format(list(set1.intersection(set2))))
print("Intersection between two sets using & operator: {}".format(list(set1 & set2)))
print({1,2,3} == {2,1,3})

