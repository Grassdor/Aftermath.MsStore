from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import store.accessory.api
from config import get_settings

settings = get_settings()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def entry():
    __store = "EVC Group"
    return {'store': __store}

app.include_router(store.accessory.api.router)
