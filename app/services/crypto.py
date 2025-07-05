from cryptography.fernet import Fernet
from app.core import Config

config = Config.get_config()
FERNET_KEY = config.FERNET_KEY.encode("utf8")


def encrypt(plaintext: str) -> str:
    """
    Encrypt `plaintext` using `secret_key` and return a URL-safe Base64 token.
    """
    cipher = Fernet(FERNET_KEY)
    encrypted_bytes = cipher.encrypt(plaintext.encode("utf-8"))
    return encrypted_bytes.decode("utf-8")


def decrypt(token: str) -> str:
    """
    Decrypt `token` (a URL-safe Base64 string) using `secret_key` and return the original text.
    """
    cipher = Fernet(FERNET_KEY)
    decrypted_bytes = cipher.decrypt(token.encode("utf-8"))
    return decrypted_bytes.decode("utf-8")
