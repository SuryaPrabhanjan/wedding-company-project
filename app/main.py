 # app/main.py
from fastapi import FastAPI
from .routes import org, admin

app = FastAPI(title="Organization Management Service")

app.include_router(admin.router)
app.include_router(org.router)
