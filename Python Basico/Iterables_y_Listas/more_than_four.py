print(" ")
size = int(input("Enter the size of the list: "))
list = []
more_than_four = []
for i in range(size):
    elem1 = input(f"Enter element {i+1} for list: ")
    list.append(elem1)
    if len(elem1) > 4:
        more_than_four.append(elem1)

print(" ")
print("The elements with more than four characters are:")
print(more_than_four)

