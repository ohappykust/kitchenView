from functools import lru_cache

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from kitchenView.core.config import get_config

config = get_config()
engine = create_engine(config.POSTGRES_HTTP_URI)


@lru_cache
def create_session() -> scoped_session:
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return session
