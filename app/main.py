
import uvicorn

from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from fastapi import RedirectResponse

from app.routers.data import data_router
from app.routers.webui import webui_router

app = FastAPI()

app.include_router(data_router, prefix="/v1")
app.include_router(webui_router, prefix="")

app.mount("/public", StaticFiles(directory="public"), name="static")

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/home", status_code=status.HTTP_303_SEE_OTHER)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
