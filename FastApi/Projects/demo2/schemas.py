from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., gt=0)


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True