from fastapi import FastAPI

from codereviewai.api.review import router as review_router
from codereviewai.api.index import router as index_router

app = FastAPI()

app.include_router(review_router, prefix="/api/v1")
app.include_router(index_router, prefix="/api/v1")
