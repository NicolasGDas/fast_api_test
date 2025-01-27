from fastapi import APIRouter, Query
from services.flight_service import fetch_flight_events, find_valid_journeys
from schemas.flight_schema import JourneySchema

router = APIRouter()

@router.get("/journeys/search")
async def search_journeys(
    origin: str = Query(..., alias="from"),
    destination: str = Query(..., alias="to"),
    date: str = Query(...)
):
    events = fetch_flight_events()
    journeys = find_valid_journeys(events, origin, destination, date)
    
    schema = JourneySchema(many=True)
    return schema.dump([{"connections": len(j), "path": j} for j in journeys])
