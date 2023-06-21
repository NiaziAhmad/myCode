# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
num = int(input("Enter a number: "))
for i in range(num):
    for j in range(num * 2):
        if num - i <= j <= num + i:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
