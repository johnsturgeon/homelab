from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.services.auth import verify_token

router = APIRouter()
security = HTTPBearer()


@router.get("/refresh_updates")
def refresh_updates(_: HTTPAuthorizationCredentials = Depends(verify_token)):
    return {"success": True}
