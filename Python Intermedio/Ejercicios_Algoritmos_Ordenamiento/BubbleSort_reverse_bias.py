def bubble_sort_reverse_bias(list):
        sorted_list = list.copy()
        n = len(sorted_list)
        for i in range(n, 0, -1):
            swapped = False
            for j in range(n-i,0,-1):
                if sorted_list[j] < sorted_list[j-1]:
                    sorted_list[j], sorted_list[j-1] = sorted_list[j-1], sorted_list[j]
                    swapped = True
            if not swapped:
                break
        return sorted_list