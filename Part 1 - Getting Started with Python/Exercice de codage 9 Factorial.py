import math

def factorial(n):
    return math.factorial(n)

try:
    n = int(input("Enter a number: "))
    print("The factorial of", n, "is: ", factorial(n))
except ValueError:
    print("Error, please enter numeric input")