'''
Enter your name: Zain ElHashemite

Enter the Stevens Honor Code: I pledge my honor I have abided by the Stevens Honor Code




'''

# Homework Assignment Three; Fall 2022

# Problem One
def main():
    print("Homework Assignment Three")

    def length():
        length = 0
        string = input("Enter a string: ")

        for i in string:
            length = length + 1

        print("The length of '", string, "' is ", length)

    # Problem Two

    def fibby():
        fib = int(input("Enter the maximum number of the Fibonacci sequence: "))
        n1 = 0
        n2 = 1

        while fib + 1 > 0:
            print(n1, end=" ")

            n3 = n1 + n2
            n1 = n2
            n2 = n3

            fib -= 1


    #Problem Three

    def age():
        years = int(input("How many years will you be entering? "))

        for i in range(0, years):
            born = int(input("What year were you born? "))
            future = int(input("For which year past the present year do you wish to determine your age? "))
            if future < 2022:
                print("Enter a year in the future")
                future = int(input("For which year past the present year do you wish to determine your age? "))
                age = future - born
                print("You will be ", age, " years old in ", future)
            else:
                age = future - born
                print("You will be ", age, " years old in ", future)


main()








