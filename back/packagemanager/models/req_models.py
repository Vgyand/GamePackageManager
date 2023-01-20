from pydantic import BaseModel


class CreatePackage(BaseModel):
    # Stuff for adding a package to db
    name: str
    description: str
    download_link: str
    size: float


class UpdatePackage(BaseModel):
    # Stuff for updating
    id: int
    name: str | None
    description: str | None
    download_link: str | None
    size: float | None
