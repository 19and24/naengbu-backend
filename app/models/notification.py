from sqlalchemy import String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from app.database import Base


class Notification(Base):
    __tablename__ = "notification"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    fridge_item_id: Mapped[int] = mapped_column(
        ForeignKey("fridge_item.id", ondelete="CASCADE"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
    )

    notify_time: Mapped[str] = mapped_column(
        DateTime,
    )

    read: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )
