from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# CORS setup to allow your Vercel frontend to fetch
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Elasticity API is live."}

@app.get("/elasticity")
async def elasticity():
    # Mock elasticity simulation — replace with real PyTorch model later
    price = round(random.uniform(9, 99), 2)
    base_demand = 1000
    elasticity_coefficient = round(random.uniform(-1.5, -0.3), 2)
    demand = round(base_demand * (1 + elasticity_coefficient * ((price - 50) / 50)))

    return {
        "model": "elasticity-v1.0.0",
        "status": "online",
        "price": price,
        "demand": demand,
        "elasticity": elasticity_coefficient,
        "timestamp": "2025-10-11T14:00:00Z"
    }
