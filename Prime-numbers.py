#Program to print prime numbers

a = int(input("Enter a number upto which you want to search: "))
for a in range(2, a):
    for i in range(2, a):
        if a % i == 0:
            break
    else:
        print(a, end = " ")
