# Write a program that asks for a number
# It would ask this many times to enter an integer
# If all the integers are entered, it should print the sum and average of these
# integers like:
# Sum: 22, Average: 4.4
num = int(input("Enter a number: "))
i = 0
total_sum = 0
while i < num:
    temp = int(input(f"Enter {i} Integer: "))
    total_sum += temp
    i += 1

print(f"Sum: {total_sum} , Average: {total_sum / num}")
