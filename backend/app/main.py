from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.app.data.router import router as router_database
from backend.app.elasticsearch.router import router as router_elastic


app = FastAPI(
    title="Map App API"
)

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.mount("/photos", StaticFiles(directory=r"parser\photos"), name="photos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT", "OPTIONS"],
    allow_headers=["Content-Type", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)


app.include_router(router_database)
app.include_router(router_elastic)
