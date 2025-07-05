from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.services import crypto
from app.core.config import Config

router = APIRouter()
security = HTTPBearer()
config = Config.get_config()


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != config.API_AUTH_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing token"
        )


@router.get("/encrypt/{plain_text}")
def encrypt_secret(
    plain_text: str, _: HTTPAuthorizationCredentials = Depends(verify_token)
):
    return {"encrypted": crypto.encrypt(plain_text)}


@router.get("/decrypt/{encrypted_text}")
def decrypt_secret(
    encrypted_text: str,
    _: HTTPAuthorizationCredentials = Depends(verify_token),
):
    return {"decrypted": crypto.decrypt(encrypted_text)}
