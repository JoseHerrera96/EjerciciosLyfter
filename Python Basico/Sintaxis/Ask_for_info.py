# Request user data
name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

# Determine age category
if age < 1:
    category = "baby"
elif age < 6:
    category = "child"
elif age < 12:
    category = "preteen"
elif age < 18:
    category = "teenager"
elif age < 30:
    category = "young adult"
elif age < 65:
    category = "adult"
else:
    category = "senior"

# Show result
print(f"\n{name} {last_name}, you are a {category}.")