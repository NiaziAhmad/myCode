# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was
num = int(input("please enter number of lines: "))
for i in range(num):
    for j in range(num):
        if i == 0 or i == num - 1 or j == 0 or j == num - 1:
            print("#", end="")
        elif i == j:
            print("#", end="")
        else:
            print(" ", end="")
    print("")
