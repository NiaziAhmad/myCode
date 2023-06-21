# - Create a variable named `numbers`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements of `numbers` programmatically
# - Print the elements of the reversed `numbers`:
#   [7, 6, 5, 4, 3]
numbers = [3, 4, 5, 6, 7]
num2 = []
size = len(numbers)
print(numbers)
for i in range(size):
    numbers[i], numbers[size - i - 1] = numbers[size - i - 1], numbers[i]

print(numbers)
