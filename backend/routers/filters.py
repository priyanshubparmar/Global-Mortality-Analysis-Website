# from fastapi import APIRouter
# from backend.database import con

# router = APIRouter()

# @router.get("/filters")
# def get_filters():

#     locations = con.execute(
#         "SELECT DISTINCT location FROM mortality_data ORDER BY location"
#     ).df()["location"].tolist()

#     years = con.execute(
#         "SELECT DISTINCT Year FROM mortality_data ORDER BY Year"
#     ).df()["Year"].tolist()

#     ages = con.execute(
#         "SELECT DISTINCT Age FROM mortality_data ORDER BY Age"
#     ).df()["Age"].tolist()

#     genders = con.execute(
#         "SELECT DISTINCT gender FROM mortality_data ORDER BY gender"
#     ).df()["gender"].tolist()

#     return {
#         "locations": locations,
#         "years": years,
#         "ages": ages,
#         "genders": genders
#     }



# from fastapi import APIRouter
# from backend.database import con

# router = APIRouter()

# @router.get("/filters")
# def get_filters():
    
#     locations = con.execute(
#         "SELECT DISTINCT location FROM mortality_data ORDER BY location"
#     ).df()["location"].tolist()

#     years = con.execute(
#         "SELECT DISTINCT Year FROM mortality_data ORDER BY Year"
#     ).df()["Year"].tolist()

#     ages = con.execute(
#         "SELECT DISTINCT Age FROM mortality_data ORDER BY Age"
#     ).df()["Age"].tolist()

#     genders = con.execute(
#         "SELECT DISTINCT gender FROM mortality_data ORDER BY gender"
#     ).df()["gender"].tolist()

#     return {
#         "locations": locations,
#         "years": years,
#         "ages": ages,
#         "genders": genders
#     }



from fastapi import APIRouter
from backend.database import con

router = APIRouter()

FILTER_COLUMNS = {
    "locations": "location",
    "years": "Year",
    "ages": "Age",
    "genders": "gender"
}

@router.get("/filters")
def get_filters():

    filters = {}

    for key, column in FILTER_COLUMNS.items():

        query = f"""
        SELECT DISTINCT {column}
        FROM mortality_data
        ORDER BY {column}
        """

        filters[key] = con.execute(query).df()[column].tolist()

    return filters