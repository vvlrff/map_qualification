from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.auth.schemas import UserRead, UserCreate
from app.auth.base_config import auth_backend, fastapi_users
from app.data_collection.router import router as router_collect
from app.get_data.router import router as router_get
from app.delete_data.router import router as router_delete
from app.elasticsearch.router import router as router_elastic


app = FastAPI(
    title="Map App API"
)

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.mount("/photos", StaticFiles(directory=r"app\photos"), name="photos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["Content-Type", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_collect)
app.include_router(router_get)
app.include_router(router_elastic)
app.include_router(router_delete)
