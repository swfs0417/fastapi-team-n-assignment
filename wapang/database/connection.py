from typing import Generator, Any
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from wapang.database.settings import DB_SETTINGS


Engine = create_engine(
    DB_SETTINGS.url,
    pool_recycle=28000,
    pool_size=10,
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(
    bind=Engine,
    autocommit=False,
    autoflush=True,
    expire_on_commit=False,
)


def get_db_session() -> Generator[Session, Any, None]:
    session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
