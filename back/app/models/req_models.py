from pydantic import BaseModel


class create_package(BaseModel):
    # Stuff for adding a package to db
    name: str
    description: str
    download_link: str
    size: float
