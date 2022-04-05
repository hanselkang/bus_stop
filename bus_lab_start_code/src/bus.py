class Bus:
    def __init__(self,input_number, input_destination):
        self.route_number = input_number
        self.destination = input_destination
        self.passengers = 0
        self.passengers_list = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return self.passengers

    def pick_up(self,person):
        self.passengers += 1
        self.passengers_list.append(person)

    def drop_off(self,person):
        self.passengers -= 1
        self.passengers_list.remove(person)

    def empty(self):
        self.passengers = 0

    def pick_up_from_stop(self,bus_stop): 
        for passenger in bus_stop.queue:
            self.passengers_list.append(passenger)
        self.passengers = len(self.passengers_list)