from pydantic import BaseModel

class Character(BaseModel):
    name: str
    gender: str
    roles: list[str]
    species: list[str]
    regions: list[str]
    resource = str
    range = str
    release_date = int
    character_img_url = str
