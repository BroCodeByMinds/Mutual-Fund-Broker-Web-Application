from pydantic import BaseModel, EmailStr

class UserCreateVM(BaseModel):
    email: EmailStr
    password: str

class UserLoginVM(BaseModel):
    email: EmailStr
    password: str

class TokenVM(BaseModel):
    access_token: str
    token_type: str = "bearer"
