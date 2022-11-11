from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt

oauth2_schema = OAuth2PasswordBearer(tokenUrl="TOKEN")

# openssl rand -hex 32
MY_SECRET_KEY = '48f48fa1ec920c7f0bc27877efa92fbdd0a7cd7d7e87d8af3cd692c97293e5a6'

ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 10

def create_access_token(data = dict , expires_delta : Optional[timedelta] = None):
	to_encoding = data.copy()
	if expires_delta:
		expire = datetime.utcnow() + expires_delta
	else:
		expire = datetime.utcnow() + timedelta(minutes=10)
	to_encode.update({"exp": expire})
	JWT_encoded = jwt.encode(to_encoding , MY_SECRET_KEY , algorithm=ALGORITHM)
	return JWT_encoded

