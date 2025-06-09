import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.health_check import router as health_check_router
from app.api.v1.user import router as user_router
from app.api.v1.sample import router as sample_router
from app.api.v1.debug import router as debug_router

app = FastAPI(
    title="Sample API",
    description="This is a simplified API server with health check, user, and avatar endpoints",
    version="1.0.0"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=health_check_router)
app.include_router(router=user_router)
app.include_router(router=sample_router)
app.include_router(router=debug_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8100, reload=True)
