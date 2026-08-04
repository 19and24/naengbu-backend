from datetime import datetime
from typing import Any

from sqlalchemy import asc, desc, func, select
from sqlalchemy.orm import Session, joinedload

from app.models.notification import Notification
from app.models.fridge_item import FridgeItem


SORT_COLUMNS = {
    "notifyTime": Notification.notify_time,
}

def get(db: Session, noti_id: int) -> Notification | None:
    return db.scalar(
        select(Notification)
        .options(joinedload(Notification.fridge_item_id))
    )