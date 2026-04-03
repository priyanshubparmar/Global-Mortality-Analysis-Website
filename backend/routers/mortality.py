# /mortality... logic and calculation. 


# Receive filter parameters
# ↓
# Build SQL filter conditions
# ↓
# Run query
# ↓
# Return result


from typing import Optional
from backend.services.mortality_service import run_analysis
from fastapi import APIRouter, Query
from backend.services.mortality_service import mortality_test_data

router = APIRouter(
    prefix="/mortality",
    tags=["Mortality"]
)

#test
@router.get("/test")
def mortality_test():

    data = mortality_test_data()

    return {
        "status": "success",
        "data": data
    }


# # 1 universal filtering
# @router.get("/analysis")
# def mortality_analysis(
#     group_by: str = "Year",
#     location: str | None = None,
#     gender: str | None = None,
#     type: str | None = None,
#     age_min: int | None = None,
#     age_max: int | None = None,
#     year_min: int | None = None,
#     year_max: int | None = None,
# ):

#     filters = {
#         "type": [type] if type else None,
#         "location": [location] if location else None,
#         "gender": [gender] if gender else None,

#         "numeric": {
#             "Age": {"min": age_min, "max": age_max},
#             "Year": {"min": year_min, "max": year_max},
#         }
#     }

#     group_columns = [g.strip() for g in group_by.split(",")]

#     data = run_analysis(filters, group_columns)

#     return {
#         "status": "success",
#         "data": data
#     }


# second universal end point

# helper function
def split_values(value: Optional[str]):
    if not value:
        return None
    return [v.strip() for v in value.split(",")]


@router.get("/analysis")
def mortality_analysis(

    group_by: str = Query("Year"),

    # categorical filters
    location: Optional[str] = Query("World"),
    type: Optional[str] = None,
    gender: Optional[str] = None,

    # age filters
    age_values: Optional[str] = None,
    age_min: Optional[int] = None,
    age_max: Optional[int] = None,

    # year filters
    year_values: Optional[str] = None,
    year_min: Optional[int] = None,
    year_max: Optional[int] = None,

    # population filters
    population_min: Optional[int] = None,
    population_max: Optional[int] = None,

    # death filters
    death_min: Optional[int] = None,
    death_max: Optional[int] = None,

    # mortality filters
    mortality_min: Optional[float] = None,
    mortality_max: Optional[float] = None
):

    filters = {

        "location": split_values(location),
        "type": split_values(type),
        "gender": split_values(gender),

        "numeric": {

            "Age": {
                "values": split_values(age_values),
                "min": age_min,
                "max": age_max
            },

            "Year": {
                "values": split_values(year_values),
                "min": year_min,
                "max": year_max
            },

            "Population": {
                "min": population_min,
                "max": population_max
            },

            "Death": {
                "min": death_min,
                "max": death_max
            }
        },

        "mortality": {
            "min": mortality_min,
            "max": mortality_max
        }
    }

    group_columns = [g.strip() for g in group_by.split(",")]

    data = run_analysis(filters, group_columns)

    return {
        "status": "success",
        "data": data
    }