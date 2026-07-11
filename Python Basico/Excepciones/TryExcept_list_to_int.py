def convert_to_integer(numbers):
    result = []
    
    for element in numbers:
        try:
            result.append(int(element))
            print(f"Successfully converted: {element}")
        except ValueError:
            print(f"Could not convert element: {element}")
    
    return result


if __name__ == "__main__":
    print(" ")
    numbers = ["10", "20", "abc", "30", "xyz", "40"]
    print(f"Original list: {numbers}")
    print(" ")
    converted = convert_to_integer(numbers)
    print(" ")
    print(f"Converted elements: {converted}")
