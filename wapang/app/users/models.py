from sqlalchemy.orm import Mapped, mapped_column
from uuid6 import uuid7
from sqlalchemy import String
from wapang.database.common import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid7()))
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)
    nickname: Mapped[str | None] = mapped_column(String(30), nullable=True)
    address: Mapped[str | None] = mapped_column(String(150), nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String(20), nullable=True)
