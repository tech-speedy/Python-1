#Program to print the below pattern
# #
# ##
# ###
# ####
# #####

a = 5
for i in range(1, a + 1):
  for j in range(1, i + 1):
    print("#", end ="")
  print()
