#Write a Python function to calculate the factorial of a number (a nonnegative integer) 

def fact(num):
    fact = 1
    if num < 0:
        print("Sorry, factorial does not exit for negative numbers")
    elif num == 0:
        print("The Factorial of  0 is 1")
    else:
        for i in range(1, num + 1):
            fact = fact * i
        print("The Factorial of ",num,"is",fact)
n1 = int(input("Enter a number:"))
fact(n1)