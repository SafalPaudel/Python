def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

#Fibonacci Sequence
# f0 = 0
# f1 = 2
# f2 = f1 + f0
# fn = f(n-1)+ f(n-2)

