# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
i = 0
a = []
sumT = 0
for i in range(0, 5):
    temp = (int(input("enter an integer number " + str(i + 1) + " : ")))
    sumT += temp
    i += 1

print(f"Sum: {sumT} , Average: {sumT / 5}")
