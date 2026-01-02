def fact(a):
    factorial = 1
    for i in range(1,a+1):
        factorial *= i

    return factorial

n = int(input("Enter the Number :- "))
print("\nFactorial of",n,"is :",fact(n))