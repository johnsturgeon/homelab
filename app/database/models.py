from sqlmodel import Field, SQLModel


class AppInfo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    app_name: str = Field(index=True, unique=True)
    server: str
    installed_version: str
    latest_version: str
