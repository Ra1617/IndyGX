from fastapi import FastAPI
from .api.contact_information_routes import router

app = FastAPI(title="Contact & Engagement Service")

app.include_router(router)
