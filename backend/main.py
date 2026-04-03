# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from backend.routers import mortality

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(mortality.router)


# @app.get("/")
# def root():
#     return {"message": "Mortality API running"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import life_table
from backend.routers import mortality
from backend.routers import filters

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mortality.router)
app.include_router(filters.router)

app.include_router(life_table.router)

@app.get("/")
def home():
    return {"message": "Mortality API running"}

