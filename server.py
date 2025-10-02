import os
import shutil
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Storage settings
LIMIT_MB = 300
STORAGE_DIR = "/data"

os.makedirs(STORAGE_DIR, exist_ok=True)

def get_storage_usage():
    total, used, free = shutil.disk_usage(STORAGE_DIR)
    used_mb = used / (1024 * 1024)
    return used_mb

@app.get("/health")
def health():
    used_mb = get_storage_usage()
    return {
        "status": "ok",
        "used_mb": used_mb,
        "limit_mb": LIMIT_MB,
        "percent": min((used_mb / LIMIT_MB) * 100, 100)
    }

# Serve frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")
