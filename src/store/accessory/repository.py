from sqlalchemy import select

from store.accessory.models import Accessory
from store.repository.base import BaseRepository


class AccessoryRepo(BaseRepository):

    MODEL = Accessory

    async def select(self, item_id: int | None = None, limit: int | None = None, *args, **kwargs):
        """
        Select queries for accessories

        Params:
            (optional) item_id: int - ID of item to be selected
            (optional) limit: int - count of records to be selected

        Returns:
            Single MODEL instance or list of MODEL instances
        """
        if not item_id:
            result = await self.session.execute(select(self.MODEL).order_by(self.MODEL.price.desc()).limit(limit))
            return result.scalars().all()
        else:
            stmt = select(self.MODEL).where(self.MODEL.id == item_id)
            result = await self.session.execute(stmt)
            return result.scalar_one()
