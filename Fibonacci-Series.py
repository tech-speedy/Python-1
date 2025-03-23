#Program to print fibonacci numbers

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end = " ")
        a, b = b, a + b
        
c = int(input("Enter a number: "))
fibonacci(c)
