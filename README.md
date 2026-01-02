# Assign-3_Functions-Modules-in-Python-

TASK 1

Functionality of the Program

Defines a function

def fact(a):


A function named fact is defined.

It takes one parameter a, which represents the number whose factorial is to be calculated.

Initializes a variable

factorial = 1


The variable factorial is used to store the result.

It starts from 1 because factorial multiplication begins from 1.

Calculates the factorial using a loop

for i in range(1, a+1):
    factorial *= i


The loop runs from 1 to a.

Each value is multiplied with factorial.

Returns the result

return factorial


The function returns the calculated factorial value.

Takes user input

n = int(input("Enter the Number :- "))


The user enters a number.

The value is stored in the variable n.

Displays the result

print("\nFactorial of", n, "is :", fact(n))


The function fact(n) is called.

The factorial of the number is printed.



TASK 2

Functionality of the Program

Imports the math module

import math


This allows the program to use built-in mathematical functions such as square root, logarithm, and trigonometric functions.

Takes user input

n = int(input("Enter the Number :- "))


The program asks the user to enter a number.

The value is converted to an integer and stored in n.

Calculates the square root

print("\nSquare Root :", math.sqrt(n))


Computes the square root of the given number.

Calculates the natural logarithm

print("Natural log :", math.log(n, math.e))


Calculates the natural logarithm (log base e) of the number.

Calculates the sine

print("Sine :", math.sin(n))


Calculates the sine of the number.

The value of n is treated as radians, not degrees.
