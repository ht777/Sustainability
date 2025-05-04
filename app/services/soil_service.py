# soil_service.py: Mocked soil fertility data retrieval
async def get_soil_fertility(location: dict) -> dict:
    """Mocked function to retrieve soil fertility data (replace with real API/database)"""
    return {
        "nitrogen": 20.5,  # mg/kg
        "phosphorus": 15.2,  # mg/kg
        "potassium": 180.0,  # mg/kg
        "ph": 6.8
    }