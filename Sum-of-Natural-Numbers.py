#Program to print the sum of first n natural numbers

num = int(input("Enter the number upto which you want to add: "))
if num < 0:
  print("Please enter a positive integer!")
else:
  sum = 0
  while (num > 0):
    sum += num
    num -= 1
    print("The sum is ", sum)
