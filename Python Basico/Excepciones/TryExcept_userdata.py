def get_user_data():
    print(" ")
    try:
        name = input("Enter your name: ")
        print(" ")

        if name.isdigit():
            raise TypeError("Name cannot be a number.")
        
        age = input("Enter your age: ")
        print(" ")

        if not age.isdigit():
            raise ValueError("Age must be a number.")
        if int(age) < 0:
            raise ValueError("Age cannot be negative.")
        
        print(f"Hello, {name}! You are {age} years old.")
    except ValueError as e:
        raise ValueError(e)
    except TypeError as e:
        raise TypeError(e)


def main():
    print(" ")
    while True:
        try:
            get_user_data()
            break
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
