from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import scoped_session
from starlette import status

from kitchenView.core.deps import get_session

from kitchenView.core.config import get_config
from kitchenView.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

SECRET_KEY = get_config().SECRET_KEY
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=180)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_pin(plain_pin, hashed_pin):
    return pwd_context.verify(plain_pin, hashed_pin)


def get_pin_hash(pin):
    return pwd_context.hash(pin)


def authenticate_user(db: scoped_session, user_id: int, pin: str) -> User | bool:
    if not (user := db.query(User).filter(User.id == user_id).first()):
        return False
    if user.pin is not None and not verify_pin(pin, user.pin):
        return False
    return user


def get_current_user(request: Request):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(request.cookies.get("session", ""), SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    db = next(get_session())
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user
