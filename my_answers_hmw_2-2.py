'''
Enter your name: Zain ElHashemite

Enter the Stevens Honor Code: I pledge my honor 




'''

# Homework Assignment Two; Fall 2022

# Problem One
def num():
    num = -11
    for i in range(1, 11):
        num = num + 1
        print(num)

# Problem Two
def multiply():
    y = eval(input("Enter a number"))
    for i in range(1, 11):
        x = y * i
        print(x)

#Problem Three
def divthree():
    for i in range(0,31):
        if i%3==0:
            print(i)

#Problem Four
def uppercount():
    x = eval(input("Enter the upper limit"))
    y = eval(input("Enter what you would like to count by"))

    for i in range(0, x + 1):
        if i % y == 0:
            print(i)

#Problem Five
import math
def squares():

    x = eval(input("How many numbers will you be entering? "))

    for i in range (0,x):
        y = eval(input("Enter number: "))
        sq = y * y
        root = math.sqrt(y)
        print("The square of ",y," is: ",sq," and the sqaure root of ",y," is: ",root)

