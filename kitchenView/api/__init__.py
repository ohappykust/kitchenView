from fastapi import APIRouter

from kitchenView.api.user import router as users_router
from kitchenView.api.recipe import router as recipes_router

router = APIRouter(prefix="/api")
router.include_router(users_router, prefix="/users", tags=["Users"])
router.include_router(recipes_router, prefix="/recipes", tags=["Recipes"])
