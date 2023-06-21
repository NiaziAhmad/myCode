# We are going to represent our contacts in a map where both the
# keys and values are strings.

# Create a map with the following key-value pairs:

contacts = {"William A. Lathan": "405-709-1865",
            "John K. Miller": "402-247-8568",
            "Hortensia E. Foster": "606-481-6467",
            "Amanda D. Newland": "319-243-5613",
            "Brooke P. Askew": "307-687-2982"}
# Create an application which prints out the answers to the following questions:
# What is John K. Miller's phone number?
print(contacts.get("John K. Miller", "No number by this Name"))
# Whose phone number is 307-687-2982?
for k, v in contacts.items():
    if v == "307-687-2982":
        print(k)
        break
# Do we know Chris E. Myers' phone number? (yes/no)
if "Chris E. Myers" in contacts:
    print("Yes")
else:
    print("No")
# The full output of your main method should be the following:

# 402-247-8568
# Brooke P. Askew
# no
