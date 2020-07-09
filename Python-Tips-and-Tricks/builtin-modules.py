import sys
import os
import random
## sys module
print(sys.version)
print(sys.argv)
print(sys.maxsize)

## os module
print(os.path)
print(os.getcwd())
print(os.path.join("C:\\", "NewFolder"))
print(os.path.exists("E:\\"))
filepath = "E:\\file"
# print(os.remove("filepath")) # to remove a path
# print(os.rmdir("directory path")) # To remove a directory
print(os.path.split(filepath))

## random module
print(random.randrange(10))  #generates numbers within first 10 numbers
print(random.randrange(0,50,5)) # generates numbers between 0 to 50 with a step value of 5
print(random.randint(0, 20))  # generates a random integer number

from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)


##