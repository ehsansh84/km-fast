from fastapi import APIRouter, status, HTTPException, Response
from datetime import datetime, timedelta

from app.db_models.user import User
from app.classes.test_cleaner import TestCleaner
from jose import jwt
import os
module_name = 'debug'
module_text = 'Debug'
router = APIRouter(
    prefix=f"/{module_name}",
    tags=[module_name]
)
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(days=3650)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, os.getenv("JWT_SECRET_KEY"), algorithm=os.getenv("JWT_ALGORITHM"))
    return encoded_jwt

@router.get("/test_token/{username}", response_description="Get token for a user")
async def get_test_token(username: str, response: Response):
    user = User()
    result = user.list({'username': username})
    if len(result) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No test user found!',
        )
    token = create_access_token(data={'app_name': 'Sudoku', 'app_version': 'v1.0.0', 'user_id': str(result[0]._id)})
    response.headers["Authorization"] = f"Bearer {token}"

    return {
        'detail': 'Test token created',
        'user_id': str(result[0]._id)
    }

@router.get("/db_clean", response_description="Initialize test data")
async def clean_db():

    TestCleaner.init_users()
    TestCleaner.clear_test_samples()

    return {
        'detail': 'Test data has been initialized.'
    }
