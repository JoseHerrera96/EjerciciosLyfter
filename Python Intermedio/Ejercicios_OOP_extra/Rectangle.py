class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive numbers.")
    

    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
