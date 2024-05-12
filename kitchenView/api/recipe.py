from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import scoped_session
from starlette import status

from kitchenView.utils import parse_pydantic_schema
from kitchenView.core.deps import get_session
from kitchenView.core.security import (
    get_current_user,
    User
)
from kitchenView.models.recipe import Recipe
from kitchenView.schemas.user import UserSchema
from kitchenView.schemas.recipe import RecipeList, RecipeCreateSchema, RecipeSchema

from kitchenView.integrations.edaru import EdaRuRecipeIntegration

router = APIRouter()


@router.get("/search", response_model=RecipeList)
async def search(
        query: str,
        external: bool = False,
        user: User = Depends(get_current_user),
) -> list[dict]:
    if not external:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
    return await EdaRuRecipeIntegration().search(query)


@router.post("/", response_model=RecipeSchema)
def create_recipe(
        data: RecipeCreateSchema,
        db: scoped_session = Depends(get_session),
        user: User = Depends(get_current_user),
) -> dict:
    db_recipe = Recipe(**parse_pydantic_schema(data))
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


@router.put("/{recipe_id}", response_model=UserSchema)
def save_recipe(
        recipe_id: int,
        db: scoped_session = Depends(get_session),
        user: User = Depends(get_current_user),
) -> dict:
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    user.recipes.append(db_recipe)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user