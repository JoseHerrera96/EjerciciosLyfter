print(" ")
my_list = [1, 2, 3, 4, 5, 3, 6, 3]
min_value = my_list[0]

for num in my_list:
    if num < min_value:
        min_value = num

print("The minimum value in the list is:", min_value)
