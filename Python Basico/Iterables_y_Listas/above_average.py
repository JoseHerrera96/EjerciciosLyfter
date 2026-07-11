print(" ")
my_list = [1, 2, 3, 4, 5, 3, 6, 3]
average= 0
highers = []

for num in my_list:
    average += num

average = average / len(my_list)

for num in my_list:
    if num > average:
        highers.append(num)

print("The average is:", average)
print("The numbers above the average are:", highers)
