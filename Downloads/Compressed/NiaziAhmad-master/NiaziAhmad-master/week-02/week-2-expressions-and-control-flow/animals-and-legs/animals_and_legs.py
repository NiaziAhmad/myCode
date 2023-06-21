# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs owned by the farmer
# It should print how many legs all the animals have
num1 = int(input("Please enter an Integer number (chickens):"))
num2 = int(input("Please enter an Integer number 2(Pigs):"))
total = (num1 * 2) + (num2 * 4)
print("total number of legs are: ", total)
print(f"{num2 > num1}")
