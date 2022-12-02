from pydantic import BaseModel


class Package(BaseModel):
    id: int | None = None
    name: str | None = None
    description: str | None = None
    download_link: str | None = None
    like_count: int | None = None
    download_count: int | None = None


class ListOfPackages(BaseModel):
    # list of packages client receives upon changing pages
    # Or applying filters
    __root__: dict[str, dict[str, str]]


class EnteringMainPage(BaseModel):
    side_link: str | None = None

    # starting_package_list: ListOfPackages | None = None
    #  list of packages client receives upon loading the main page


class Message(BaseModel):
    __root__: dict[str, str]
