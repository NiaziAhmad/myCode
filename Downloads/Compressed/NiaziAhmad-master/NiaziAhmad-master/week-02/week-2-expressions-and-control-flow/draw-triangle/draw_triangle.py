# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was
num = int(input("Enter a number: "))
for i2 in range(num):
    for j in range(num, i2, -1):
        print("*", end="")
    print()
#     *******
#     *****
#     ****
#     ***
#     *
# for i in range(num):
#     for j in range(num, i, -1):
#         print(" ", end="")
#     for k in range(i + 1):
#         print("*", end="")
#     print("l")
#           *
#          **
#         ***
#       *****
#     *******

# for i in range(num):
#     for k in range(i + 1):
#         print("*", end="")
#     print("l")
#     *
#     **
#     ***
#     ****
#     ******
#
# for i in range(num):
#     for k in range(i):
#         print(" ", end="")
#     for j in range(i, num, 1):
#         print("*", end="")
#     print("l")
#     *******
#      ******
#       *****
#        ****
#          **
#           *

# for i in range(num):
#     for j in range(num, i, -1):
#         print(" ", end="")
#     # if i == 0:
#     #     print("*", end="")
#     for k in range(i+1):
#         print("*", end="")
#     for k in range(i):
#         print("*", end="")
#     print("l")
#
# for i2 in range(num):
#     for j in range(num, i2, -1):
#         print(" ", end="")
#     # if i == 0:
#     #     print("*", end="")
#     for k in range(i2+1):
#         print("*", end="")
#     for k in range(i):
#         print("*", end="")
#     print("l")
