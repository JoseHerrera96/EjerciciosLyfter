def bubble_sort_steps(lst):
    iterations = 0
    swaps = 0
    sorted_list = lst.copy()
    n = len(sorted_list)
    for i in range(n):
        iterations += 1
        swapped = False
        for j in range(0, n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                swapped = True
                swaps += 1
        if not swapped:
            break
    print(f"Sorted list: {sorted_list}")
    print(f"Iterations: {iterations}")
    print(f"Swaps: {swaps}")
    return sorted_list