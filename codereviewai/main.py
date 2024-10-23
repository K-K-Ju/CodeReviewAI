from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from codereviewai.api.review import router as review_router
from codereviewai.api.index import router as index_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["http://localhost:8000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(review_router, prefix="/api/v1")
app.include_router(index_router, prefix="/api/v1")
