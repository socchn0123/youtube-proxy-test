from fastapi import FastAPI, Request
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.routers import video

app = FastAPI()

app.include_router(video.router)

app.mount("/static", StaticFiles(directory="app/templates"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("app/templates/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
