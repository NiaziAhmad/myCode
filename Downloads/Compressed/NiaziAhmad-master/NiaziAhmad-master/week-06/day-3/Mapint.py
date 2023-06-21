# Create a map where the keys are strings and the values are strings with the 
# following initial values | Key | Value | |
#:---------------- | :---------------------- | | 
# 978-1-60309-452-8 | A Letter to Jo | |
# 978-1-60309-459-7 | Lupus | |
# 978-1-60309-444-3 | Red Panda and Moon Bear | |
# 978-1-60309-461-0 | The Lab |
my = {"978-1-60309-452-8": "A Letter to Jo",
      "978-1-60309-459-7": "Lupus",
      "978-1-60309-444-3": "Red Panda and Moon Bear",
      "978-1-60309-461-0": "The Lab"}

# Print all the key-value pairs in the following format
for k, v in my.items():
    print(f"{v} (ISBN: {k})")
# A Letter to Jo (ISBN: 978-1-60309-452-8)
# Lupus (ISBN: 978-1-60309-459-7)
# Red Panda and Moon Bear (ISBN: 978-1-60309-444-3)
# The Lab (ISBN: 978-1-60309-461-0)
# Remove the key-value pair with key 978-1-60309-444-3
my.pop("978-1-60309-444-3")
# Remove the key-value pair with value The Lab
for key, value in my.items():
    if value == "The Lab":
        del my[key]
        break

my.update({"978-1-60309-450-4": "They Called Us Enemy",
           "978-1-60309-453-5": "Why Did We Trust Him?"})
# Print whether there is an associated value with key 478-0-61159-424-8 or not
print(my.pop("478-0-61159-424-8", "false"))
# Print the value associated with key 978-1-60309-453-5
print(my.pop("978-1-60309-453-5", "false"))
