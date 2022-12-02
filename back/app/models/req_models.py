from pydantic import BaseModel


class create_package(BaseModel):
    # Stuff for adding a package to db
    name: str
    description: str
    download_link: str


class delete_package(BaseModel):
    # Id to delete a package with corresponding id
    package_id: int


class add_like_down(BaseModel):
    # Add +1 to like or download count
    package_id: int
