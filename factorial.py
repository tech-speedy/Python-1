#Program to calculate the factorial of a given integer

a = int(input("Enter an integer: "))

factorial = 1
for i in range (1, a + 1):
  factorial *= i
print("The factorial of a given integer is:", factorial)
