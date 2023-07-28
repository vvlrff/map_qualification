from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.schemas import UserRead, UserCreate
from app.auth.base_config import auth_backend, fastapi_users

from app.data_collection.router import router as router_collect
from app.news_classification.router import router as router_classif
from app.delete_data.router import router as router_delete

app = FastAPI(
    title="Map App"
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
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
app.include_router(router_classif)
app.include_router(router_delete)

