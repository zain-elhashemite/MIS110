'''
Name:Zain ElHashemite  
Date: 11/18/2022
Pledge: I pledge my honor that I have abided by the Stevens Honor Code.
'''

# Problem 1

def main():
    def names():
        infileName = input("File with names: ")
        outfileName = input("Destination file: ")
        infile = open(infileName, "r")
        outfile = open(outfileName, "w")

        for i in infile:
            first, last = i.split()
            name = (first + " " + last).upper()
            print(name, file=outfile)
        infile.close()
        outfile.close()
        print("Names have been written to:", outfileName)
main()





# Problem 2

def conditionalSquares():
    def sqsums(mylist):
        list2 = []
        odd = []
        even = []
        for i in mylist:
            x = i ** 2
            list2.append(x)
        for i in list2:
            if i % 2 != 0:
                odd.append(i)
            elif i % 2 == 0:
                even.append(i)
        if len(odd) > 0:
            print(even)

        elif len(odd) == 0:
            y = 0
            for i in even:
                y += i
            print(y)
conditionalSquares():

    

# Problem 3

def add(x, y):
    sum1 = x + y
    return sum1

def sub(x, y):
    dif1 = x - y
    return dif1

def mul(x, y):
    pro1 = x * y
    return pro1

def div(x, y):
    quo1 = x / y
    return quo1

def calc():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    func = (input("What would you like to do? Add, Subtract, Multiply, or

    if func == "Add" or func == "add":
    sum2 = add(x, y)
    print(sum2)

    elif func == "Subtract" or func == "subtract":
    dif2 = sub(x, y)
    print(dif2)

    elif func == "Multiply" or func == "multiply":
    pro2 = mul(x, y)
    print(pro2)

    elif func == "Divide" or func == "divide":
    quo2 = div(x, y)
    print(quo2)

    cont = (input("Would you like to continuing using the calculator? "))

    if cont == "Yes" or cont == "yes":
        calc()
















