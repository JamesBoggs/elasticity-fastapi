from ops_instrumentation import attach_ops
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import numpy as np

app = FastAPI()
attach_ops(app)

# Allow CORS from your portfolio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Elasticity API running"}

@app.get("/elasticity")
async def elasticity():
    # Simulate price-demand data (could be replaced with real CSV data later)
    prices = np.linspace(20, 120, 6)  # e.g. $20 → $120
    true_elasticity = -1.2            # true hidden elasticity
    base_demand = 1000

    # Simulate realistic demand curve with some randomness
    demands = base_demand * (prices / 50) ** true_elasticity + np.random.normal(0, 25, size=len(prices))

    # Fit a linear regression in log-log space
    log_price = np.log(prices)
    log_demand = np.log(np.maximum(demands, 1))  # avoid log(0)
    slope, intercept = np.polyfit(log_price, log_demand, 1)

    # Predicted elasticity = slope coefficient
    elasticity_estimate = round(slope, 3)

    # Pick an average point to report
    avg_price = float(np.mean(prices))
    avg_demand = float(np.mean(demands))

    return {
        "model": "elasticity-v2.0.0",
        "status": "online",
        "lastUpdated": str(datetime.utcnow().isoformat()),
        "data": {
            "prices": [round(p, 2) for p in prices.tolist()],
            "demands": [round(d, 2) for d in demands.tolist()],
            "avgPrice": round(avg_price, 2),
            "avgDemand": round(avg_demand, 2),
            "elasticityEstimate": elasticity_estimate
        }
    }
