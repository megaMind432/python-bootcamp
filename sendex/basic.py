# Print Function and Strings - 0
"""
print() is a function that is used for debugging purpose or if anything needs to be printed in the console.
The passed parameter's are known as String in python. If one tries to print something with quotes than we need
to print it use double quotes inside a single quote. Example:
print("I'm feeling sick") or
print(' I\'m feeling sick')

"""
print("This is an example of print function")

# String concatenation
print("Abdullah " + "Al " + "Mehedi")
print("Abdullah ", "Al ", "Mehedi")

# We can not concate number with string
# print("Abdullah " + 5)
# In order to concate number and string we need to convert type
print("Abdullah " + str(5))
print("Abdullah " + "5")

# Math operations
print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5)
# This will provide the remainder
print(5 % 5)
# We can not do
# print(int('5.0' + 5))

# Math operations - 1
'''
Used Math operation or symbols
+ - * / %
special : exponent **

'''

# Variables - 2
'''
Variables are place holder and that can be vary on different input's or output's. There is no need to declare
the type of the variable. We can make a variable in python with just the name of the variable. We can use 
variable with function .

we can also use packing:
x,y = (2, 3)
print(x) will produce 2
print(y) will produce 3

we can't do:
x,y = (2, 3, 5)
this produce error
'''

# While Loop - 3
'''
It is also known as game loop 
'''
condition = 1
while condition < 8:
    print(condition)
    # increment operator
    condition += 1

# Infinite Loop - It always runs
while True:
    print("Infinite loop")


# For Loop - 4
'''
range() is a built in function that produce the number between the range
range(1, 3) will produce: 1,2,3
'''
for i in range(4):
    print(i)

# This will iterate through the number and print everything in  the List
exampleList = [1, 2, 3, 5, 8, 13, 21]
for eachNumber in exampleList:
    print(eachNumber)

# If Statement - 5

'''
Assignment operator:

symbol   |     name
---------|------------------------
>        | Greater than
---------|------------------------
<        | Less than
---------|------------------------
>=       | Greaterthan or equal
---------|------------------------
<=       | Less than or equal
---------|------------------------
!=       | Not equal
---------|------------------------
==       | Is equal
---------|------------------------

* If statement will only work if the condition is true. If the condition is not true than it will not run.
'''
x = 01
y = 10

if x != y:
    print("Is not equal.")
if x >= y:
    print("x is greater than or equal to y")
if x <= y:
    print("X is less than or equal to y")
if x == y:
    print("x is equal to y")


# If Else - 5
'''
** It is like if something is true than run that or if block of code otherwise run the else block of code

'''
x = 01
y = 10

if x > y:
    print("If it satisfy than it will run")
else:
    print("This will run if x>y is false")


# Else If - 6
'''
** It is also the alternative of multiple if statement
*** In elif condition order of operation is 'Important'

'''

x = 01
y = 10
z = 001
if x > y:
    print("True if")
elif x < y:
    print("1'st elif True")
elif x == y:
    print("2'nd elif work")
else:
    print("Nothing is work")

# Function - 7

'''
** Function is important for any kind of programming language. It is mainly the verb of any program. In order 
to complete a sentence mu must have to have verbs which is the main thing for making a sentence so function is 
also the same thing. The syntax of making function is :
def __nameOfFunction:
    working principles

'''
# function defination


def function():
    print("This is inside the function")
    x = 10
    y = 20
    return x+y


# function call
function()

# Function Parameters - 8


def simple_addition(x, y):
    sum = x+y
    return sum


print(simple_addition(10, 20))

# Function Parameters Default - 9


def simple_(num1, num2):
    pass


def simple(num1, num2=10):
    print(num1, num2)


simple(10)
