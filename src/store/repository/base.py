from abc import ABC, abstractmethod

from pydantic import BaseModel
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.base import Base

from .exceptions import NotFoundException


class BaseRepository(ABC):
    """Abstract base repository class"""

    MODEL: Base

    def __init__(self, session: AsyncSession):
        self.session = session

    @abstractmethod
    async def select(self, item_id: int | None = None, limit: int | None = None, *args, **kwargs):
        """Get objects by item ID if set else all with limit"""

    async def insert(self, item: BaseModel | dict, *args, **kwargs):
        """Insert object"""
        db_item = self.MODEL(**item.model_dump())
        self.session.add(db_item)
        await self.session.commit()
        await self.session.refresh(db_item)
        return db_item

    async def update(self, item_id: int, item: BaseModel | dict, *args, **kwargs):
        """Update item by item ID"""
        db_item = await self.select(item_id=item_id)
        if not db_item:
            raise NotFoundException
        for attr, value in item.model_dump(exclude_unset=True).items():
            setattr(db_item, attr, value)
        self.session.add(db_item)
        await self.session.commit()
        await self.session.refresh(db_item)
        return db_item

    async def delete(self, item_id: int, *args, **kwargs):
        """Delete object by item ID"""
        result = await self.session.execute(delete(self.MODEL).where(self.MODEL.id == item_id))
        if result.rowcount == 0:
            raise NotFoundException
        await self.session.commit()
