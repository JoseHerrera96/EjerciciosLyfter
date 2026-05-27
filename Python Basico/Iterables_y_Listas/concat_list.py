print(" ")
size = int(input("Enter the size of the lists: "))
list1 = []
list2 = []
for i in range(size):
    elem1 = input(f"Enter element {i+1} for list1: ")
    list1.append(elem1)
for i in range(size):
    elem2 = input(f"Enter element {i+1} for list2: ")
    list2.append(elem2)
print(" ")
for index in range(0,len(list2)):
    print(list1[index]," ", list2[index])
