from datetime import datetime

class FlightEvent:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = datetime.strptime(departure_time, "%Y-%m-%d %H:%M")
        self.arrival_time = datetime.strptime(arrival_time, "%Y-%m-%d %H:%M")
