from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from kitchenView.models import Base
from kitchenView.models.recipe import Recipe


recipes_association = Table(
    'recipes_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('recipe_id', Integer, ForeignKey('recipes.id'))
)


class User(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column()
    pin: Mapped[str] = mapped_column(nullable=True)
    recipes: Mapped[list["Recipe"]] = relationship('Recipe', secondary=recipes_association, lazy="joined")
    is_admin: Mapped[bool] = mapped_column(default=False)
