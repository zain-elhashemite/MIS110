def main():
    print("This program illustrates a chaotic function")
    n = eval(input("How many numbers do you want to have printed? "))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
main()
