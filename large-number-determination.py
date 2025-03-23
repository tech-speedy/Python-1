#Program to print the largest of three numbers

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if c > b and c > a:
    print("The last number is the greater number")
elif b > c and b > a:
    print("The second number is the greater number")
elif a > c and a > b:
    print("The first number is the greater number")
elif a == b and b == c:
    print("All numbers are equal")
elif c > b and c == a:
    print("The last and first number is equal")
elif b > c and b == a:
    print("The first and second number is equal")
