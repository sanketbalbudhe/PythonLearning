'''
Task 1: Calculate Factorial Using a Function
def Factorial(n):
    if n <= 1:
        return 1
    return n * Factorial(n-1)


a = int(input("Enter a number: "))

print ("Factorial of {} is:{}".format(a,Factorial(a)))
'''
'''
Task 2: Using the Math Module for Calculations
'''
import math

def sqrroot(n):
    return math.sqrt(n)

def log(n):
    return math.log(n)

def sine(n):
    return math.sin(n)


a = int(input("Enter a number: "))
print ("Square root: ",sqrroot(a))
print ("Logarithm: ",log(a))
print ("Sine: ",sine(a))
