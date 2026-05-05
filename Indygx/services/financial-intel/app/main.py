from fastapi import FastAPI
from .api.financials_routes import router

app = FastAPI(title="Financial Intelligence Service")

app.include_router(router)
