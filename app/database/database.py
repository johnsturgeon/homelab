from sqlalchemy import Engine
from sqlmodel import SQLModel, create_engine


def get_engine() -> Engine:
    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    connect_args = {"check_same_thread": False}
    return create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(get_engine())
