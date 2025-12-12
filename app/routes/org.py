# app/routes/org.py
from fastapi import APIRouter, HTTPException, Depends
from ..models import OrgCreate, OrgUpdate, OrgDelete
from ..crud import create_organization, get_organization, delete_organization, master_db
from ..utils import hash_password
from ..deps import get_current_admin

router = APIRouter(prefix="/org", tags=["Organization"])

@router.post("/create")
def org_create(payload: OrgCreate):
    org = create_organization(payload.organization_name, payload.email, hash_password(payload.password))
    if not org:
        raise HTTPException(status_code=400, detail="Organization already exists")
    return {"success": True, "organization": {"name": org["organization_name"], "collection": org["collection_name"]}}

@router.get("/get")
def org_get(organization_name: str):
    org = get_organization(organization_name)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return {"organization_name": org["organization_name"], "collection_name": org["collection_name"], "admin_id": str(org["admin_id"])}

@router.delete("/delete")
def org_delete(payload: OrgDelete, admin=Depends(get_current_admin)):
    org = get_organization(payload.organization_name)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    if str(org["admin_id"]) != admin["admin_id"]:
        raise HTTPException(status_code=403, detail="Not authorized")
    delete_organization(payload.organization_name)
    return {"success": True, "message": f"Organization {payload.organization_name} deleted"}
