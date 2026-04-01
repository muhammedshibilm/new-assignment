from fastapi import FastAPI
from app.api.router import router as api_router
from app.db.session import Base, engine
from app import models

app = FastAPI(
    title="New Assignment API",
    version="1.0.0",
)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)

#  Health check endpoint
@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "healthy"}


app.include_router(api_router , prefix="/api", tags=["API Endpoints"])