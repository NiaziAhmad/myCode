# We are going to represent our expenses in a list containing integers.

# Create a list with the following items:
# 500, 1000, 1250, 175, 800 and 120
expenses = [500, 1000, 1250, 175, 800, 120]
# Create an application which prints out the answers to the following questions:
# How much did we spend?
print(sum(expenses))
# Which was our greatest expense?
print(max(expenses))
# Which was our cheapest spending?
print(min(expenses))
# What was the average amount of our spendings? (print this as a float value)
print(f"{(sum(expenses) / len(expenses)):.4f}")
# The full output of your main method should be the following:

# 3845
# 1250
# 120
# 640.8333
