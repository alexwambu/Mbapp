import os
import psutil
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve frontend static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Storage settings
STORAGE_LIMIT_MB = int(os.getenv("STORAGE_LIMIT_MB", "300"))
BUILDER_LIMIT_MB = int(os.getenv("BUILDER_LIMIT_MB", "500"))

@app.get("/")
def read_index():
    return FileResponse("static/index.html")

@app.get("/storage")
def get_storage():
    usage = psutil.disk_usage("/")
    used_mb = usage.used // (1024 * 1024)
    percent = round((used_mb / STORAGE_LIMIT_MB) * 100, 2)
    return {
        "storage_limit_mb": STORAGE_LIMIT_MB,
        "used_mb": used_mb,
        "percent_used": percent
    }
