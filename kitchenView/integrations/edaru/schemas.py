from pydantic import BaseModel, Field


class RecipeComponentMeasureUnit(BaseModel):
    name: str
    name_five: str
    name_two: str

    def __init__(self, **kwargs):
        kwargs["name_five"] = kwargs["nameFive"]
        kwargs["name_two"] = kwargs["nameTwo"]
        super().__init__(**kwargs)


class RecipeComponent(BaseModel):
    amount: float
    name: str
    measure_unit: RecipeComponentMeasureUnit

    def __init__(self, **kwargs):
        kwargs["name"] = kwargs["ingredient"]["name"]
        kwargs["measure_unit"] = kwargs["measureUnit"]
        super().__init__(**kwargs)


class RecipeStep(BaseModel):
    description: str
    image_url: str | None

    def __init__(self, **kwargs):
        kwargs["image_url"] = kwargs["imageUrl"]
        super().__init__(**kwargs)


class RecipeNutritionInfo(BaseModel):
    carbohydrates: float
    fats: float
    kilocalories: float
    proteins: float


class ERRecipe(BaseModel):
    name: str
    image_url: str = Field(source="recipeCover.imageUrl")
    components: list[RecipeComponent]
    category: str
    kitchen: str | None
    portions_count: float
    preparation_time_minutes: int
    cooking_time_minutes: int
    likes: int
    dislikes: int
    steps: list[RecipeStep]
    nutrition_info: RecipeNutritionInfo

    def __init__(self, **kwargs):
        body = kwargs["node"]
        kwargs["name"] = body["name"]
        kwargs["image_url"] = body["recipeCover"]["imageUrl"]
        kwargs["components"] = body["composition"]
        kwargs["category"] = body["recipeCategory"]["name"]
        kwargs["kitchen"] = body["cuisine"]["name"] if "cuisine" in body.keys() and body["cuisine"] is not None else None
        kwargs["likes"] = body["likes"]
        kwargs["dislikes"] = body["dislikes"]
        kwargs["portions_count"] = body["portionsCount"]
        kwargs["preparation_time_minutes"] = body["preparationTime"]
        kwargs["cooking_time_minutes"] = body["cookingTime"]
        kwargs["steps"] = body["recipeSteps"]
        kwargs["nutrition_info"] = body["nutritionInfo"]

        super().__init__(**kwargs)


class ERRecipesList(BaseModel):
    recipes: list[ERRecipe]

    def __init__(self, **kwargs):
        kwargs["recipes"] = kwargs["data"]["recipes"]["edges"]
        super().__init__(**kwargs)
