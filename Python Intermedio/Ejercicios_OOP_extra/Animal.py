class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("make a sound.")


class Dog:
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def speak(self):
        print("Guau!")

class Cat:
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def speak(self):
        print("Miau!")