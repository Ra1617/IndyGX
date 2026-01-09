from fastapi import FastAPI
from backend.api.company_routes import router as company_router


app = FastAPI(
    title="IndyGX Company Intelligence API",
    version="1.0.0",
)

@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok"}

# Register routers
app.include_router(
    company_router,
    prefix="/companies",
    tags=["companies"]
)
 