print(" ")
my_list = [1, 2, 3, -4, 5, 3, 6, 3]
min_value = my_list[0]
negative_flag=False

for num in my_list:
    if num < 0:
        print("There are at least one non-positive number in the list.")
        negative_flag=True
        break
        
if negative_flag==True:
    pass
else:
    print("All numbers are positive.")
