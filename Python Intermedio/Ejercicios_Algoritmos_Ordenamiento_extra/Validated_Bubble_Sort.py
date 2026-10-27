def Validated_Bubble_Sort(list):
    if len(list) == 0:
        print("Empty list provided")
        return False
    #validate that list are numbers
    for item in list:
        if not isinstance(item, (int, float)):
            print(f"Invalid item in list: {item}. List must contain only numbers.")
            return False
    if len(list) >= 2:
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
    else:
        return list
    return sorted_list