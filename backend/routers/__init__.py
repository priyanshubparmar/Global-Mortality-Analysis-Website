from fastapi import APIRouter
from backend.services.mortality_service import mortality_test_data

router = APIRouter(
    prefix="/mortality",
    tags=["Mortality"]
)

@router.get("/test")
def mortality_test():

    data = mortality_test_data()

    return {
        "status": "success",
        "data": data
    }