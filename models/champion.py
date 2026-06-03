from pydantic import BaseModel, Field

class Character(BaseModel):
    name: str = Field(serialization_alias="championName")
    gender: str
    roles: list[str]
    species: list[str]
    regions: list[str]
    resource: str
    range: str
    release_date: int = Field(serialization_alias="releaseDate")
    character_img_url: str = Field(serialization_alias="characterImgUrl")
    