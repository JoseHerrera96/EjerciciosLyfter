def validate_bubble_sort(list):
    if list is None:
        return False
    if len(list) < 2:
        return False
    #validate that list are numbers
    for item in list:
        if not isinstance(item, (int, float)):
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