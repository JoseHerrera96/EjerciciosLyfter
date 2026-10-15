def bubble_sort_steps(lst):
    Iterations = 0
    Swaps = 0
    sorted_list = list.copy()
    n = len(sorted_list)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                swapped = True
                Swaps += 1
        if not swapped:
            break
        Iterations += 1
    print(f"Sorted list: {sorted_list}")
    print(f"Iterations: {Iterations}")
    print(f"Swaps: {Swaps}")
    return sorted_list