from person import person

class Bus:
    passengers
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
    
    def add_passenger(self, passenger: person):
        if len(self.passengers) >= self.max_passengers:
            print("Bus is full")
            return
        self.passengers.append(passenger)
        print(f"{passenger.name} added to bus")

    def remove_passenger(self, passenger: person):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"{passenger.name} removed from bus")
        else:
            print(f"{passenger.name} is not on bus bus")    
    
