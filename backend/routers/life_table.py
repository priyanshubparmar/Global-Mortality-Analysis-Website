from fastapi import APIRouter
from backend.services.life_table_service import get_life_table

router = APIRouter(
    prefix="/life-table",
    tags=["Life Table"]
)

@router.get("/analysis")
def life_table_analysis(
    location: str,
    gender: str,
    year: int,
    age: int
):
    return get_life_table(location, gender, year, age)
