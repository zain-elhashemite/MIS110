import math
def squares():

    x = eval(input("How many numbers will you be entering? "))

    for i in range (0,x):
        y = eval(input("Enter number: "))
        sq = y * y
        root = math.sqrt(y)
        print("The square of ",y," is: ",sq," and the sqaure root of ",y," is: ",root)