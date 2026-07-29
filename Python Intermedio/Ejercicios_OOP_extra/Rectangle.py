class Rectangle:
    def __init__(self):
        while(True):
            try:
                if self.width <= 0 or self.height <= 0:
                    raise ValueError
                self.width = input("Enter the width of the rectangle: ")
                self.height = input("Enter the height of the rectangle: ")
                break
            except ValueError:
                print("Width and height must be positive numbers.")
    

    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
