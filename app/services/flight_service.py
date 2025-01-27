import requests
from config import FLIGHT_EVENTS_API_URL
from utils.helpers import within_limits
from schemas.flight_schema import FlightSchema

def fetch_flight_events():
    """ Obtiene la lista de eventos de vuelo desde la API. """
    # response = requests.get(FLIGHT_EVENTS_API_URL)
    # return response.json()
    return  [
  {
    "flight_number": "IB1234",
    "departure_city": "MAD",
    "arrival_city": "BUE",
    "departure_datetime": "2021-12-31T23:59:59.000Z",
    "arrival_datetime": "2022-01-01T10:00:00.000Z"
  },
  {
    "flight_number": "IB5678",
    "departure_city": "BUE",
    "arrival_city": "SCL",
    "departure_datetime": "2022-01-01T12:00:00.000Z",
    "arrival_datetime": "2022-01-01T15:00:00.000Z"
  },
  {
    "flight_number": "IB9101",
    "departure_city": "SCL",
    "arrival_city": "LIM",
    "departure_datetime": "2022-01-01T17:00:00.000Z",
    "arrival_datetime": "2022-01-01T20:00:00.000Z"
  },
  {
    "flight_number": "IB1122",
    "departure_city": "LIM",
    "arrival_city": "MIA",
    "departure_datetime": "2022-01-02T08:00:00.000Z",
    "arrival_datetime": "2022-01-02T14:00:00.000Z"
  },
  {
    "flight_number": "IB3344",
    "departure_city": "MIA",
    "arrival_city": "JFK",
    "departure_datetime": "2022-01-02T16:00:00.000Z",
    "arrival_datetime": "2022-01-02T19:00:00.000Z"
  },
  {
    "flight_number": "IB4455",
    "departure_city": "MAD",
    "arrival_city": "CDG",
    "departure_datetime": "2022-01-01T09:00:00.000Z",
    "arrival_datetime": "2022-01-01T11:00:00.000Z"
  },
  {
    "flight_number": "IB5566",
    "departure_city": "CDG",
    "arrival_city": "FRA",
    "departure_datetime": "2022-01-01T12:30:00.000Z",
    "arrival_datetime": "2022-01-01T14:00:00.000Z"
  },
  {
    "flight_number": "IB6677",
    "departure_city": "LHR",
    "arrival_city": "JFK",
    "departure_datetime": "2022-01-03T10:00:00.000Z",
    "arrival_datetime": "2022-01-03T14:00:00.000Z"
  },
  {
    "flight_number": "IB7788",
    "departure_city": "FRA",
    "arrival_city": "LAX",
    "departure_datetime": "2022-01-03T18:00:00.000Z",
    "arrival_datetime": "2022-01-03T23:00:00.000Z"
  },
  {
    "flight_number": "IB8899",
    "departure_city": "LAX",
    "arrival_city": "SYD",
    "departure_datetime": "2022-01-04T08:00:00.000Z",
    "arrival_datetime": "2022-01-05T17:00:00.000Z"
  },
  {
    "flight_number": "IB12321",
    "departure_city": "MAD",
    "arrival_city": "SYD",
    "departure_datetime": "2022-01-01T23:30:59.000Z",
    "arrival_datetime": "2022-01-02T10:00:00.000Z"
  },
  {
    "flight_number": "IB5678",
    "departure_city": "SYD",
    "arrival_city": "SCL",
    "departure_datetime": "2022-01-02T13:00:00.000Z",
    "arrival_datetime": "2022-01-02T20:00:00.000Z"
  },
  {
    "flight_number": "IB12321",
    "departure_city": "MAD",
    "arrival_city": "SCL",
    "departure_datetime": "2022-01-01T23:30:59.000Z",
    "arrival_datetime": "2022-01-02T20:00:00.000Z"
  },
]


def find_valid_journeys(events, origin, destination, date):
    """ Busca viajes válidos basados en las restricciones. """
    date = date + " "
    schema = FlightSchema()
    events = [schema.load(e) for e in events if e['departure_datetime'] >= date]
    journeys = []
    flights_of_journey = []
    for first_leg in events:
        print(first_leg)
        if first_leg['departure_city'] == origin:
            if first_leg['arrival_city'] == destination:
                # Viaje directo
                journeys.append([first_leg])
            else:
                # Buscar conexiones
                for second_leg in events:
                    if (first_leg['arrival_city'] == second_leg['departure_city'] and 
                        second_leg['arrival_city'] == destination
                        and within_limits(first_leg, second_leg)):
                        print("Hola")
                        journeys.append([first_leg, second_leg])

    return journeys

