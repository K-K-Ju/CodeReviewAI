from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI

from codereviewai.api.review import router as review_router

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     httpx.get('')
#     yield

app = FastAPI()

app.include_router(review_router, prefix="/api/v1")


@app.get("/")
async def index():
    return {"Hello": "World"}
