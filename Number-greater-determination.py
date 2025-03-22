#Program to determine which is greater than two numbers

a = float(input("Enter a number: "))
b = float(input("Enter a number: "))

if (a > b):
  print("First number is a greater number")
elif (b > a):
  print("Second number is a greater number")
elif (b == a):
  print("Both are equal numbers")
else:
  print("Print enter a valid integer.")
