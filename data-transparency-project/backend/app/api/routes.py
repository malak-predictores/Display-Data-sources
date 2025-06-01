from fastapi import APIRouter
from app.services.imf import get_imf_data
from app.services.europa import get_europa_data
from app.services.swiss import get_swiss_data

router = APIRouter(prefix="/data", tags=["data"])

@router.get("/all")
async def get_all_data():
    return {
        "imf": await get_imf_data(),
        "europa": await get_europa_data(),
        "swiss": await get_swiss_data(),
    }
