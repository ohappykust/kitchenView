from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    """
    Base class for other models
    """
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
