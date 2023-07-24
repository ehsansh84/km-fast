import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
from fastapi import FastAPI
import uvicorn
from app.api.user import router as user_router

app = FastAPI()
app.include_router(router=user_router)

if __name__ == "__main__":
    uvicorn.run("boot:app", host="0.0.0.0", port=8000, reload=True)
