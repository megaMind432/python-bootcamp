#!/usr/bin/python
"""
* Writing on files or Making text file and write on the file
"""

# Writing to a file

# text = "Hello world! This is \nNew Line"
# open is universal for working with the file
# saveFile = open('exampleFile.txt', 'w')
# saveFile.write(text)
# saveFile.close()

# Appending file or writing extra thing to the maden file

# appendMe = '\nNew bit of information'

# appendFile = open('exampleFile.txt', 'a')
# appendFile.write(appendMe)
# appendFile.close()

# For reading file
# readMe = open('exampleFile.txt', 'r').read()
# print(readMe)

# readMe = open('exampleFile.txt', 'r').readlines()
# print(readMe)

'''
Class in python 3
'''


class Calculator:

    def addition(self, x, y):
        added = x+y
        print(added)

    def subtraction(x, y):
        sub = x+y
        print(sub)

    def multiplication(x, y):
        mult = x*y
        print(mult)

    def divison(x, y):
        div = x/y
        print(div)


Calculator.multiplication(2, 3)
