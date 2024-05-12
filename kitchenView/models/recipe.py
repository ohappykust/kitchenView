from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from kitchenView.models import Base


class RecipeComponentMeasureUnit(Base):
    __tablename__ = "recipe_component_measure_units"
    recipe_component_id: Mapped[int] = mapped_column(ForeignKey("recipe_components.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column()
    name_five: Mapped[str] = mapped_column()
    name_two: Mapped[str] = mapped_column()


class RecipeComponent(Base):
    __tablename__ = "recipe_components"
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id", ondelete="CASCADE"))
    amount: Mapped[float] = mapped_column()
    name: Mapped[str] = mapped_column()
    measure_unit: Mapped["RecipeComponentMeasureUnit"] = relationship(backref="recipe_component", lazy="joined")


class RecipeStep(Base):
    __tablename__ = "recipe_steps"
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id", ondelete="CASCADE"))
    description: Mapped[str] = mapped_column()
    image_url: Mapped[str] = mapped_column(nullable=True)


class RecipeNutritionInfo(Base):
    __tablename__ = "recipe_nutrition_infos"
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id", ondelete="CASCADE"))
    carbohydrates: Mapped[float] = mapped_column()
    fats: Mapped[float] = mapped_column()
    proteins: Mapped[float] = mapped_column()
    kilocalories: Mapped[float] = mapped_column()


class Recipe(Base):
    __tablename__ = "recipes"
    name: Mapped[str] = mapped_column()
    image_url: Mapped[str] = mapped_column(nullable=True)
    components: Mapped[list[RecipeComponent]] = relationship(backref="recipe", lazy="joined")
    category: Mapped[str] = mapped_column()
    kitchen: Mapped[str] = mapped_column(nullable=True)
    portions_count: Mapped[float] = mapped_column()
    preparation_time_minutes: Mapped[int] = mapped_column()
    cooking_time_minutes: Mapped[int] = mapped_column()
    likes: Mapped[int] = mapped_column()
    dislikes: Mapped[int] = mapped_column()
    steps: Mapped[list[RecipeStep]] = relationship(backref="recipe", lazy="joined")
    nutrition_info: Mapped[RecipeNutritionInfo] = relationship(backref="recipe", lazy="joined")

