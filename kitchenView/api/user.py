from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import scoped_session
from starlette import status

from kitchenView.core.deps import get_session
from kitchenView.core.security import (
    authenticate_user,
    create_access_token,
    get_current_user,
    get_pin_hash
)
from kitchenView.models.user import User
from kitchenView.schemas.user import (
    UserPublicSchema,
    UserSchema,
    UserCreateSchema,
    UserLoginSchema
)

router = APIRouter()


@router.get("/", response_model=list[UserPublicSchema])
def get_all_users(
        db: scoped_session = Depends(get_session)
) -> list[dict]:
    return db.query(User).all()


@router.post("/", response_model=UserSchema)
def create_user(
        user: UserCreateSchema,
        db: scoped_session = Depends(get_session)
) -> dict:
    users = db.query(User).all()
    db_user = User(**user.dict())
    if len(users) == 0:
        db_user.is_admin = True
    if db_user.pin is not None:
        db_user.pin = get_pin_hash(db_user.pin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/me", response_model=UserSchema)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/login")
def login(
        data: UserLoginSchema,
        db: scoped_session = Depends(get_session)
) -> dict:
    if not (user := authenticate_user(db, data.id, data.pin)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect id or pin",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": create_access_token(data={"sub": user.id})}
