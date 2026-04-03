# #This file acts like a pipeline between backend and dataset.
# Service sends SQL
# ↓
# DuckDB executes query
# ↓
# Returns dataframe
#-----------------------
# import duckdb

# con = duckdb.connect()

# def run_query(query: str):
#     df = con.execute(query).df()
#     return df



import duckdb

con = duckdb.connect()

# mortality dataset
con.execute("""
CREATE OR REPLACE VIEW mortality_data AS
SELECT * FROM read_parquet('data/mortality.parquet')
""")

# disability dataset
con.execute("""
CREATE OR REPLACE VIEW disability_data AS
SELECT * FROM read_parquet('data/disability_rate_data.parquet')
""")

def run_query(query: str):
    return con.execute(query).df()