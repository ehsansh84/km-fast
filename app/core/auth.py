import os
from jose import jwt, JWTError
from fastapi import status, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from publics import Settings
module_dir = os.path.dirname(os.path.abspath(__file__))


class Token:
    def __init__(self, token=None, app_name='', app_version='', user_id='', exp=None, jwt_secret=None, jwt_algorithm=None):
        self.token = token
        self.app_name = app_name
        self.app_version = app_version
        self.user_id = user_id
        self.exp = exp
        self.jwt_secret = jwt_secret
        self.jwt_algorithm = jwt_algorithm

    def decode(self):
        try:
            payload = jwt.decode(
                token=self.token,
                options={"verify_signature": False},
                key=self.jwt_secret,
                algorithms=[self.jwt_algorithm]
            )
            self.app_name = payload['app_name']
            self.app_version = payload['app_version']
            self.user_id = payload['user_id']
            self.exp = payload['exp']
            return payload
        except JWTError:
            return None


security = HTTPBearer()


async def get_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if Settings.SHOW_TOKEN:
        print(f'cred: {credentials}')

    if credentials:
        if not credentials.scheme.lower() == "bearer":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication scheme.")
        token = Token(token=credentials.credentials)

        token.jwt_secret = os.getenv("JWT_SECRET_KEY")
        token.jwt_algorithm = os.getenv("JWT_ALGORITHM")
        if not token.decode():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return token
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authorization code.")