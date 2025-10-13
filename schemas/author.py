from pydantic import BaseModel

class AuthorCreate(BaseModel):
    name: str

class AuthorResponse(BaseModel):
    author_id: int
    name: str
    class Config:
        from_attribute = True
