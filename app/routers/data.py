from fastapi import APIRouter


data_router = APIRouter()


@data_router.get("/data")
def get_data():
    return {'data': 'data'}
