from fastapi import APIRouter
from fastapi.responses import FileResponse, HTMLResponse

webui_router = APIRouter()

@webui_router.get("/home", response_class=HTMLResponse)
def get_home_page():
    return FileResponse('public/home')
