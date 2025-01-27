from marshmallow import Schema, fields

class FlightSchema(Schema):
    flight_number = fields.Str(required=True)
    departure_city = fields.Str(data_key="departure_city", required=True)
    arrival_city = fields.Str(required=True)
    departure_datetime = fields.Str(required=True)
    arrival_datetime = fields.Str(required=True)

class JourneySchema(Schema):
    connections = fields.Int(required=True)
    path = fields.List(fields.Nested(FlightSchema))
