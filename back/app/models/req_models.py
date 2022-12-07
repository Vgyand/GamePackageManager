from pydantic import BaseModel


class create_package(BaseModel):
    # Stuff for adding a package to db
    name: str
    description: str
    download_link: str
    size: float


class update_package(BaseModel):
    # Stuff for updating
    id: int
    name: str | None
    description: str | None
    download_link: str | None
    size: float | None
