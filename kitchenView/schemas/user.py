from pydantic import BaseModel, field_validator

from kitchenView.schemas.recipe import RecipeSchema


class UserPublicSchema(BaseModel):
    id: int
    name: str
    pin: bool | None

    @field_validator('pin', mode="before")  # noqa
    @classmethod
    def set_pin_to_true(cls, v):
        if v is not None:
            return True
        return False


class UserSchema(UserPublicSchema):
    recipes: list[RecipeSchema]
    is_admin: bool


class UserCreateSchema(BaseModel):
    name: str
    pin:  str | None = None


class UserLoginSchema(BaseModel):
    id: int
    pin: str | None = None
