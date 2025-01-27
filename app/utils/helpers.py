from datetime import datetime, timedelta

def within_limits(flight1, flight2):
    """ Verifica si dos vuelos cumplen las restricciones de conexión. """
    arr_time_1 = datetime.strptime(flight1['arrival_datetime'], "%Y-%m-%dT%H:%M:%S.%fZ")
    dep_time_2 = datetime.strptime(flight2['departure_datetime'], "%Y-%m-%dT%H:%M:%S.%fZ")
    total_duration = datetime.strptime(flight2['arrival_datetime'], "%Y-%m-%dT%H:%M:%S.%fZ") - datetime.strptime(flight1['departure_datetime'], "%Y-%m-%dT%H:%M:%S.%fZ")
    
    return (dep_time_2 - arr_time_1 <= timedelta(hours=4)) and (total_duration <= timedelta(hours=24))
