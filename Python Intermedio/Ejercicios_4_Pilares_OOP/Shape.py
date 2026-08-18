from abc import abstractmethod, ABC

class Shape(ABC):
    
    def __init__(self):
        pass
        
    @abstractmethod
    def calculate_area(self):
        pass
        
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return 4 * self.side
        
