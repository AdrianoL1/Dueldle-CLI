from pydantic import BaseModel, Field

class Character(BaseModel):
    name: str
    roles: list[str]
    class_list: list[str] = Field(alias="class")
    range_type = str
    resource = str
    release_date = int
