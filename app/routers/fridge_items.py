from datetime import datetime

from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session

from app.core.responses import success
from app.dependencies import get_db
from app.schemas.fridge_item import FridgeItemCreate, FridgeItemUpdate
from app.services import fridge_item as fridge_item_service

router = APIRouter(prefix="/fridge-items", tags=["fridge-items"])


@router.get("")
def list_fridge_items(
    keyword: str | None = None,
    category: str | None = None,
    starred: bool | None = None,
    expired: bool | None = None,
    deadline_before: datetime | None = Query(None, alias="deadlineBefore"),
    sort: str = "deadline,asc",
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    data = fridge_item_service.list_items(
        db, keyword=keyword, category=category, starred=starred, expired=expired,
        deadline_before=deadline_before, sort=sort, page=page, size=size,
    )
    return success(data)


@router.get("/{item_id}")
def get_fridge_item(item_id: int, db: Session = Depends(get_db)):
    return success(fridge_item_service.get_item(db, item_id))


@router.post("", status_code=status.HTTP_201_CREATED)
def create_fridge_item(body: FridgeItemCreate, db: Session = Depends(get_db)):
    return success(fridge_item_service.create_item(db, body))


@router.patch("/{item_id}")
def update_fridge_item(
    item_id: int, body: FridgeItemUpdate, db: Session = Depends(get_db)
):
    return success(fridge_item_service.update_item(db, item_id, body))


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fridge_item(item_id: int, db: Session = Depends(get_db)):
    fridge_item_service.delete_item(db, item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
