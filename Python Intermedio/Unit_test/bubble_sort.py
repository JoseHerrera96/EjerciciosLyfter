def bubble_sort(unsort_list):
    if not isinstance(unsort_list, list):
        raise AttributeError("Input must be a list")
    sorted_list = unsort_list.copy()
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
