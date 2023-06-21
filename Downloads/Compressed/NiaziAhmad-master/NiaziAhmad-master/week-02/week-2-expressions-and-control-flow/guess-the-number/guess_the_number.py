# Write a program that stores a number and the user has to figure it out
# The user can input guesses
# After each guess the program would tell one of the following:
#
# The stored number is higher
# The stored number is lower
# You found the number: 8
choice = 40
cond = True
while cond:
    temp = int(input("input a number: 30"))
    if choice > temp:
        print("The stored number is higher")
    elif choice < temp:
        print("The stored number is lower")
    elif choice == temp:
        cond = False
        print("You found the number: ", temp)
