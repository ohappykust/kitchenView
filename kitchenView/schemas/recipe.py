from pydantic import BaseModel

from kitchenView.models.recipe import (
    Recipe,
    RecipeStep,
    RecipeComponent,
    RecipeNutritionInfo,
    RecipeComponentMeasureUnit
)


class RecipeComponentMeasureUnitSchema(BaseModel):
    name: str
    name_five: str
    name_two: str

    class Meta:
        orm_model = RecipeComponentMeasureUnit


class RecipeComponentSchema(BaseModel):
    amount: float
    name: str
    measure_unit: RecipeComponentMeasureUnitSchema

    class Meta:
        orm_model = RecipeComponent


class RecipeStepSchema(BaseModel):
    description: str | None = None
    image_url: str | None = None

    class Meta:
        orm_model = RecipeStep


class RecipeNutritionInfoSchema(BaseModel):
    carbohydrates: float
    fats: float
    kilocalories: float
    proteins: float

    class Meta:
        orm_model = RecipeNutritionInfo


class RecipeCreateSchema(BaseModel):
    name: str
    image_url: str | None
    components: list[RecipeComponentSchema]
    category: str
    kitchen: str | None
    portions_count: float
    preparation_time_minutes: int
    cooking_time_minutes: int
    likes: int
    dislikes: int
    steps: list[RecipeStepSchema]
    nutrition_info: RecipeNutritionInfoSchema

    class Meta:
        orm_model = Recipe


class RecipeSchema(RecipeCreateSchema):
    id: int | None = None


class RecipeList(BaseModel):
    recipes: list[RecipeSchema]
