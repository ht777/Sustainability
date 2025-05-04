# main.py: Entry point for the FastAPI application
from fastapi import FastAPI
from app.routers import field_router, irrigation_router

# Initialize FastAPI app
app = FastAPI(
    title="Smart Agriculture Backend",
    description="Backend for AI-powered crop and irrigation recommendations",
    version="1.0.0"
)

# Include routers for field and irrigation endpoints
app.include_router(field_router.router, prefix="/api/v1/fields", tags=["Fields"])
app.include_router(irrigation_router.router, prefix="/api/v1/irrigation", tags=["Irrigation"])

@app.get("/")
async def root():
    """Root endpoint for health check"""
    return {"message": "Smart Agriculture Backend is running"}