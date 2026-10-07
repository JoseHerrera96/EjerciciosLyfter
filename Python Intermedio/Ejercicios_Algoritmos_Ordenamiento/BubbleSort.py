def bubble_sort(list):
    sorted_list = list.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list

# Decorator to control the sorting direction of the bubble sort function
def BubbleSort_control(Bias: bool):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if Bias==True:
                print("Sorting forward enabled")
            else:
                print("Sorting backward enabled")
                result = result[::-1]
            return result
        return wrapper
    return decorator