# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000
length = float(input("Enter the length of Cuboid:"))

breadth = float(input("Enter the breadth of Cuboid:"))

height = float(input("Enter height of Cuboid:"))

area = (2 * ((length * breadth) + (breadth * height) + (height * length)))

print("Surface Area: " + area)
print(f"Volume: {length * height * area}")
