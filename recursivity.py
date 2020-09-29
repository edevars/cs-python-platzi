import sys


def factorial(n):
    """
        Calc the factorial of every positive number
        n int > 0
        return n!
    """
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial(n-1)

print(f"Recursion limit {sys.getrecursionlimit()}")

n = int(input("Write a number please: "))

print(f"The factorial of {n} is {factorial(n)}")
