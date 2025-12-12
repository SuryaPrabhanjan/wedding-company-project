# app/models.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class OrgCreate(BaseModel):
    organization_name: str
    email: EmailStr
    password: str

class OrgUpdate(BaseModel):
    old_name: str
    new_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class AdminLogin(BaseModel):
    email: EmailStr
    password: str

class OrgDelete(BaseModel):
    organization_name: str
