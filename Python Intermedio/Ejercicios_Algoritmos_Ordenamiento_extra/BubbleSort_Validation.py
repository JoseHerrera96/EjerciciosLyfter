def validatec_bubble_sort(list):
    if list is None:
        print("Empty list provided")
        return False
    if len(list) < 2:
        print("List is too short to sort")
        return False
    #validate that list are numbers
    for item in list:
        if not isinstance(item, (int, float)):
            print(f"Invalid item in list: {item}. List must contain only numbers.")
            return False
    sorted_list = list.copy()
    n = len(sorted_list)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                swapped = True
        if not swapped:
            break
    return sorted_list