from backend.database import run_query
# from backend.config import DATA_PATH

def mortality_test_data():

    query = f"""
    SELECT
        Year,
        SUM(Death) * 1000.0 / SUM(Population) AS mortality_rate
    FROM mortality_data
    GROUP BY Year
    ORDER BY Year
    """

    df = run_query(query)

    return df.to_dict(orient="records")



# def build_where(filters: dict):

#     conditions = []

#     # categorical filters
#     for col in ["type", "location", "gender"]:
#         values = filters.get(col)

#         if values:
#             value_string = ",".join([f"'{v}'" for v in values])
#             conditions.append(f"{col} IN ({value_string})")

#     # numeric filters
#     numeric = filters.get("numeric", {})

#     for column, rule in numeric.items():

#         if rule.get("min") is not None:
#             conditions.append(f"{column} >= {rule['min']}")

#         if rule.get("max") is not None:
#             conditions.append(f"{column} <= {rule['max']}")

#     if conditions:
#         return "WHERE " + " AND ".join(conditions)

#     return ""

# def run_analysis(filters: dict, group_columns: list):

#     where_clause = build_where(filters)

#     group_string = ", ".join(group_columns)

#     query = f"""
#     SELECT
#         {group_string},
#         SUM(Death) as deaths,
#         SUM(Population) as population,
#         SUM(Death) * 1000.0 / SUM(Population) AS mortality_rate
#     FROM mortality_data
#     {where_clause}
#     GROUP BY {group_string}
#     ORDER BY {group_string}
#     """

#     df = run_query(query)

#     return df.to_dict(orient="records")



from backend.database import run_query
from backend.config import DATA_PATH


# -----------------------------
# Build WHERE filters
# -----------------------------
def build_where(filters: dict):

    conditions = []

    # categorical filters
    for col in ["location", "type", "gender"]:
        values = filters.get(col)

        if values:
            value_string = ",".join([f"'{v}'" for v in values])
            conditions.append(f"{col} IN ({value_string})")

    # numeric filters
    numeric = filters.get("numeric", {})

    for column, rule in numeric.items():

        if rule.get("values"):
            vals = ",".join(map(str, rule["values"]))
            conditions.append(f"{column} IN ({vals})")

        if rule.get("min") is not None:
            conditions.append(f"{column} >= {rule['min']}")

        if rule.get("max") is not None:
            conditions.append(f"{column} <= {rule['max']}")

    if conditions:
        return "WHERE " + " AND ".join(conditions)

    return ""


# -----------------------------
# Build HAVING filters
# -----------------------------
def build_having(filters: dict):

    conditions = []

    mortality = filters.get("mortality")

    if mortality:

        if mortality.get("min") is not None:
            conditions.append(f"mortality_rate >= {mortality['min']}")

        if mortality.get("max") is not None:
            conditions.append(f"mortality_rate <= {mortality['max']}")

    if conditions:
        return "HAVING " + " AND ".join(conditions)

    return ""


# -----------------------------
# Universal analysis engine
# -----------------------------
def run_analysis(filters: dict, group_columns: list):

    where_clause = build_where(filters)
    having_clause = build_having(filters)

    group_string = ", ".join(group_columns)

    query = f"""
    SELECT
        {group_string},

        SUM(Death) AS deaths,
        SUM(Population) AS population,

        SUM(Death) * 1000.0 / SUM(Population) AS mortality_rate

    FROM mortality_data

    {where_clause}

    GROUP BY {group_string}

    {having_clause}

    ORDER BY {group_string}
    """

    df = run_query(query)

    return df.to_dict(orient="records")


# filters = {

#     "location": ["India", "Pakistan"],
#     "type": ["Country/Area"],
#     "gender": ["Male","Female"],

#     "numeric": {

#         "Age": {
#             "values": None,
#             "min": 0,
#             "max": 5
#         },

#         "Year": {
#             "values": None,
#             "min": 2000,
#             "max": 2020
#         },

#         "Population": {
#             "min": 1000000,
#             "max": None
#         },

#         "Death": {
#             "min": None,
#             "max": None
#         }
#     },

#     "mortality": {
#         "min": 5,
#         "max": None
#     }
# }