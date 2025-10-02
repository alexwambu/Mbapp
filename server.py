import os
import psutil
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# ✅ Ensure static dir exists
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")

STORAGE_LIMIT_MB = int(os.getenv("STORAGE_LIMIT_MB", "300"))

@app.get("/")
def read_index():
    index_file = "static/index.html"
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "Static index.html not found."}

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
