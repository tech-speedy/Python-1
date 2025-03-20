#Program to input marks of 3 subjects, compute average, and then calculate grades

a = int(input("Enter first subject marks: "))
b = int(input("Enter second subject marks: "))
c = int(input("Enter third subject marks: "))

average = a + b + c / 3

if (average >= 80):
  print("Level 4, above normalised standards")
elif (average <= 79):
  print("Level 3, at normalised standards")
elif (average <= 69):
  print("Level 2, below but normalised standards")
elif (average <= 59):
  print("Level 1, well below normalised standards")
elif (average <= 49):
  print("Level 1, too below normalised standards")
elif (average <= 33):
  print("Remedial standards")
