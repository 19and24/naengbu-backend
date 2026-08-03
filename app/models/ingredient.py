from datetime import datetime

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Ingredient(Base):
    __tablename__ = "ingredient"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    deadline: Mapped[datetime|None] = mapped_column(DateTime)
    category: Mapped[str|None] = mapped_column(String(120))
    emoji: Mapped[str|None] = mapped_column(String(20))
    starred: Mapped[bool] = mapped_column(Boolean, default=False)
