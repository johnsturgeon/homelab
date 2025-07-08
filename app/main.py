import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import app_updates, ansible
from app.core.config import global_config
from app.database.database import create_db_and_tables
from app.database.models import AppInfo  # noqa: F401


# Lifespan context for FastAPI
@asynccontextmanager
async def lifespan_context(_: FastAPI):
    await global_config.load_secrets()
    yield


app = FastAPI(title="Homelab API Gateway", lifespan=lifespan_context)


def include_routers(the_app: FastAPI, routers: list[tuple]):
    for router, prefix, tags in routers:
        the_app.include_router(router, prefix=prefix, tags=tags)


# Mount routers

include_routers(
    app,
    [
        (ansible.router, "/api/v1/ansible", ["Ansible"]),
        (app_updates.router, "/api/v1/app_updates", ["App Updates"]),
    ],
)
create_db_and_tables()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
