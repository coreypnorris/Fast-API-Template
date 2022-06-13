from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status
from app.data.schemas import User, UserOutput
from app.data.db import load_users_db
from dotenv import dotenv_values


security = HTTPBasic()
db = load_users_db()
config = dotenv_values(".env")


def get_authenticated_user(credentials: HTTPBasicCredentials = Depends(security)) -> UserOutput:
    result = [user for user in db if user.username == credentials.username]
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username or Password incorrect"
        )
    
    user = User(
        id=result[0].id,
        username=result[0].username,
        password_hash=config["ADMIN_PASSWORD_HASH"]
    )
    
    if user.verify_password(credentials.password) == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username or Password incorrect"
        )

    return UserOutput(id=user.id, username=user.username)