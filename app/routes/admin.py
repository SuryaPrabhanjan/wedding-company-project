 # app/routes/admin.py
from fastapi import APIRouter, HTTPException
from ..models import AdminLogin
from ..utils import verify_password
from ..crud import master_db
from ..auth import create_access_token

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/login")
def admin_login(payload: AdminLogin):
    admin = master_db.admins.find_one({"email": payload.email})
    if not admin or not verify_password(payload.password, admin["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"admin_id": str(admin["_id"])})
    return {"access_token": token, "token_type": "bearer"}
