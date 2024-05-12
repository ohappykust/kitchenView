from typing import Generator

from sqlalchemy.orm import scoped_session

from kitchenView.core.database import create_session


def get_session() -> Generator[scoped_session, None, None]:
    session = create_session()
    try:
        yield session
    finally:
        session.remove()
