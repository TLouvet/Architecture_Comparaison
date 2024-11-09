from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import date


class UserDTO(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    role: str = Field(..., pattern="^(admin|reader)$")