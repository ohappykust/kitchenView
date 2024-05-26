from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt, JWTError

from starlette import status
from fastapi import HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import scoped_session

from kitchenView.core.deps import get_session
from kitchenView.core.config import get_config
from kitchenView.models.user import User

config = get_config()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"/api/users/login"
)

SECRET_KEY = config.SECRET_KEY
ALGORITHM = "HS256"


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=180)
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


async def get_current_user(request: Request):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(await reusable_oauth2(request), SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError as e:
        print(e)
        raise credentials_exception
    db = next(get_session())
    user = db.query(User).filter(User.id == str(user_id)).first()
    if user is None:
        raise credentials_exception
    return user
