from fastapi import FastAPI
from .api.indygx_assessment_routes import router

app = FastAPI(title="IndyGX Assessment Service")

app.include_router(router)
