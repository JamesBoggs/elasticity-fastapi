from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Elasticity API is live."}

@app.get("/elasticity")
async def elasticity():
    # Mock elasticity logic for now
    price = round(random.uniform(10, 100), 2)
    base_demand = 1000
    elasticity_coefficient = round(random.uniform(-1.5, -0.3), 2)
    demand = round(base_demand * (1 + elasticity_coefficient * ((price - 50) / 50)))

    return {
        "model": "elasticity-v1.2.3",
        "status": "online",
        "price": price,
        "demand": demand,
        "elasticity": elasticity_coefficient,
        "timestamp": "2025-10-11T14:00:00Z"
    }
