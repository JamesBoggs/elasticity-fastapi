from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/elasticity")
async def elasticity():
    return {
        "model": "elasticity-v1.2.3",
        "status": "online",
        "lastUpdated": str(datetime.utcnow().date()),
        "data": {
            "price": 49.99,
            "demand": 720,
            "elasticity": -1.4
        }
    }
