from fastapi import FastAPI
from .api.competitive_intelligence_routes import router

app = FastAPI(title="Competitive Intelligence Service")

app.include_router(router)
