print(" ")
size = int(input("Enter the size of the list: "))
list = []
for i in range(size):
    elem1 = input(f"Enter element {i+1} for list: ")
    list.append(elem1)

for index, elemt in enumerate(list):
    if int(elemt) % 2 != 0:
        list.pop(index)

print(" ")
print("Odd list:", list)