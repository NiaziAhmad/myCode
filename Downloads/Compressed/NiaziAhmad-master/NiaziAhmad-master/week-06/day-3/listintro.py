list_a = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]
list_b = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]

print("Durian" in list_a)

list_b.remove("Durian")

list_a.insert(4, "Kiwifruit")

print("List A is equal to List B:", len(list_a) == len(list_b))

# Get the index of "Avocado" from List A
print(list_a.index("Avocado"))
# Get the index of "Durian" from List B
if "Durian" in list_b:
    print(list_b.index("Durian"))
else:
    print(-1)
# Add "Passion Fruit" and "Pomelo" to List B in a single statement
list_b += ["Passion Fruit", "Pomelo"]
# Print out the 3rd element from List A
print(list_a[2])
# Print all elements of List A
print(list_a)
# Print all elements of List B
print(list_b)
