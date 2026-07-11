print(" ")
size = int(input("Enter the size of the list: "))
list = []
for i in range(size):
    elem1 = input(f"Enter element {i+1} for list: ")
    list.append(elem1)

last_elem = list[-1]
fst_elem = list[0]

list[0] = last_elem
list[-1] = fst_elem

print(" ")
print("Modified lists:")
print(list)
