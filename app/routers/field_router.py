# field_router.py: Endpoints for field selection and crop recommendations
from fastapi import APIRouter, HTTPException
from app.models import FieldRequest, FieldResponse, Location  # Absolute import
from app.services import maps_service, soil_service, gemini_service  # Absolute import

router = APIRouter()

@router.post("/", response_model=FieldResponse)
async def create_field(field_request: FieldRequest):
    """Create a new field and get crop recommendations"""
    try:
        # Get field data (ID and area) from Google Maps API
        field_data = await maps_service.get_field_data(field_request.location.dict())

        # Get soil fertility data
        soil_fertility = await soil_service.get_soil_fertility(field_request.location.dict())

        # Get crop recommendations from Gemini API
        recommended_crops = await gemini_service.get_crop_recommendations(
            soil_data=soil_fertility,
            area_sqm=field_data["area_sqm"]
        )

        return FieldResponse(
            field_id=field_data["field_id"],
            location=field_request.location,
            area_sqm=field_data["area_sqm"],
            soil_fertility=soil_fertility,
            recommended_crops=recommended_crops
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing field: {str(e)}")