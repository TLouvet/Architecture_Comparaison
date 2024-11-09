from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional, Set

class AuthorDTO(BaseModel):
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    birth_date: str
    death_date: Optional[str] = None
    nationality: str = Field(..., max_length=100)
    biography: Optional[str] = Field(None, max_length=2000)
    books: List[int] = Field(default_factory=set)