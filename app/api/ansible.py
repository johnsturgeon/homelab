from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.config import global_config
from app.services.auth import verify_token
from fabric import Connection

router = APIRouter()
security = HTTPBearer()


@router.get("/new_host/{host_name}")
async def refresh_updates(
    host_name: str, _: HTTPAuthorizationCredentials = Depends(verify_token)
):
    result = await upsert_ssh_key(host_name)
    return {"result": result}


async def upsert_ssh_key(hostname: str) -> str:
    """ " Upserts the Ansible Host's public SSH key into the given host"""
    await global_config.load_secrets()
    conn = Connection(
        host=hostname,
        user="root",
        connect_kwargs={"password": global_config.ROOT_PASSWORD},
    )
    result: str = "Key already exists. No action taken"
    public_key = global_config.ANSIBLE_PUBLIC_KEY
    conn.run("mkdir -p ~/.ssh", hide=True)
    auth_keys = conn.run("cat ~/.ssh/authorized_keys || true", hide=True)
    if public_key not in auth_keys.stdout:
        result: str = "Key Added!"
        conn.run(f'echo "{public_key}" >> ~/.ssh/authorized_keys')
    return result
