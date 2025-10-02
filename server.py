from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# ✅ Mount /static folder if it exists
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index():
    """
    Try serving from /static/index.html
    If missing, fallback to static_index.html
    If both missing, show a plain message.
    """
    if os.path.exists("static/index.html"):
        return FileResponse("static/index.html", media_type="text/html")
    elif os.path.exists("static_index.html"):
        return FileResponse("static_index.html", media_type="text/html")
    else:
        return HTMLResponse("<h1>🚀 App running, but no index.html found</h1>")
        

@app.get("/health")
def health():
    return {"status": "ok", "service": "Storage/ML Editor"}
