# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was
line = int(input("Enter a number: "))
for i in range(line):
    for j in range(line, i, -1):
        print(" ", end="")
    for k in range(i - 1):
        print("*", end="")
    for l in range(i):
        print("*", end="")
    print("")
i = 0
for i in range(line):
    for j in range(i):
        print(" ", end="")
    for k in range(i, line - 1, 1):
        print("*", end="")
    for l in range(line, i, -1):
        print("*", end="")
    print("")
