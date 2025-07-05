import uvicorn
from fastapi import FastAPI
from app.api import secrets

app = FastAPI(title="Homelab API Gateway")

# Mount routers
app.include_router(secrets.router, prefix="/api/v1/secrets", tags=["Secrets"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
