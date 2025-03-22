#Program to check if the number is equal to the sum of the cubes of the digits (armstrong checking)

def cubes(n):
    cubes = sum(int(digit) ** 3 for digit in str(n))
    return cubes == n

num = int(input("Enter a number: "))
if cubes(num):
    print(f"{num} is equal to the sum of the cubes of its digits.")
else:
    print(f"{num} is NOT equal to the sum of the cubes of its digits.")
