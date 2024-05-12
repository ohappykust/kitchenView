from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from kitchenView.api import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)
