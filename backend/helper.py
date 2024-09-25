import os
from fastapi import HTTPException, Header

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


def authenticate_access_token(token: str = Header(...)):
    if token != ACCESS_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid access token")