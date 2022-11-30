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
    background_photo_link: str | None = None
    logo_link: str | None = None
    link_A: str | None = None
    link_B: str | None = None
    link_C: str | None = None

    # starting_package_list: ListOfPackages | None = None
    #  list of packages client receives upon loading the main page
