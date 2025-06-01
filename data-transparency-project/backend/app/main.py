from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as data_router

app = FastAPI(
    title="Data Transparency API",
    description="API providing data points with source attribution",
    version="1.0.0"
)

# Allow frontend React app to access backend (adjust origins as needed)
origins = [
    "http://localhost:3000",  # React dev server default
    # Add other allowed origins if deploying
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the /data router
app.include_router(data_router)

# Optional root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Data Transparency API"}

