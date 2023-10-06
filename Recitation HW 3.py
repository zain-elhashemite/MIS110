#question 1
#factorial problem

def factorial():
    n = int(input("Enter a number"))
    fact = 1
    for i in range(1,n+1):
        fact = fact *i
        print(fact)


#question 2
#star problem

def star():
    for i in range (6,0,-1):
        for j in range(i):
            print("*", end="")
        print("")


#question 3
#number = 5 problem

def isitfive():
    x = eval(input("Enter a number"))
    if x==5:
        print("Your number is equal to 5")
    else:
        print("Your number is not equal to 5")

