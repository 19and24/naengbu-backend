from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class NotificationCreate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    fridge_item_id: int = Field(alias="fridgeItemId", gt=0)
    title: str = Field(min_length=1,max_length=100)
    content: str | None = Field(default=None)
    notify_time: datetime | None = None
    read: bool = False

class NotificationUpdate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    fridge_item_id: int | None = Field(default=None, alias="fridgeItemId", gt=0)
    title: str | None = Field(default=None, min_length=1, max_length=100)
    content: str | None = Field(default=None) 
    notify_time: datetime | None = None
    read: bool | None = None