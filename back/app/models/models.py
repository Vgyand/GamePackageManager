from pydantic import BaseModel
from enum import Enum


class Package(BaseModel):
    id: int
    name: str
    description: str | None = None
    download_link: str | None = None
    like_count: int | None = None
    download_count: int | None = None
    cover_link: str | None = None


class ListOfPackages(BaseModel):
    # list of packages client receives upon changing pages
    # Or applying filters
    list_of_packages: dict[int, Package] | None = None


class EnteringMainPage(BaseModel):
    background_photo_link: str | None = None
    logo_link: str | None = None
    link_A: str | None = None
    link_A: str | None = None
    link_A: str | None = None

    # starting_package_list: ListOfPackages | None = None
    #  list of packages client receives upon loading the main page


class RespModels(Enum):
    RM_Package = Package
    RM_Package_list = ListOfPackages
    RM_MainPage = EnteringMainPage
