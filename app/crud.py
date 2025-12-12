 # app/crud.py
from pymongo import MongoClient
from .config import MONGO_URI, MASTER_DB
from bson.objectid import ObjectId

client = MongoClient(MONGO_URI)
master_db = client[MASTER_DB]

def create_organization(org_name, email, password_hash):
    if master_db.organizations.find_one({"organization_name": org_name}):
        return None
    admin_id = master_db.admins.insert_one({"email": email, "password_hash": password_hash}).inserted_id
    collection_name = f"org_{org_name}"
    master_db.create_collection(collection_name)
    org_id = master_db.organizations.insert_one({
        "organization_name": org_name,
        "collection_name": collection_name,
        "admin_id": admin_id
    }).inserted_id
    return master_db.organizations.find_one({"_id": org_id})

def get_organization(org_name):
    return master_db.organizations.find_one({"organization_name": org_name})

def delete_organization(org_name):
    org = get_organization(org_name)
    if not org:
        return None
    master_db.client[MASTER_DB].drop_collection(org["collection_name"])
    master_db.admins.delete_one({"_id": org["admin_id"]})
    master_db.organizations.delete_one({"_id": org["_id"]})
    return True
