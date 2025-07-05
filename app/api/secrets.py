from fastapi import APIRouter
from app.services import crypto


router = APIRouter()


@router.get("/encrypt/{plain_text}")
def encrypt_secret(plain_text: str):
    return {"encrypted": crypto.encrypt(plain_text)}


@router.get("/decrypt/{encrypted_text}")
def decrypt_secret(encrypted_text: str):
    return {"decrypted": crypto.decrypt(encrypted_text)}
