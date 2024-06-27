from fastapi import APIRouter, Depends, Response
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database.connection import get_session
from store.accessory.repository import AccessoryRepo
from store.accessory.schemas import Accessory, AccessoryCreate, AccessoryUpdate
from store.repository.exceptions import NotFoundException

router = APIRouter(prefix='/accessory', tags=['Accessories'])


@router.get("", response_model=list[Accessory])
async def get_accessories(limit: int | None = None, session: AsyncSession = Depends(get_session)):
    """Get list of accessories"""

    repo = AccessoryRepo(session)
    return [
        Accessory(**result.__dict__)
        for result in await repo.select(limit=limit)
    ]


@router.post("", response_model=Accessory)
async def add_accessory(
        accessory: AccessoryCreate,
        session: AsyncSession = Depends(get_session)
):
    """Add accessory"""
    repo = AccessoryRepo(session)
    result = await repo.insert(accessory)
    return Accessory(**result.__dict__)


@router.put("/{item_id}", response_model=Accessory)
async def update_book(item_id: int, item: AccessoryUpdate, session: AsyncSession = Depends(get_session)):
    """Update accessory by `id`"""
    repo = AccessoryRepo(session)
    try:
        result = await repo.update(item_id, item)
    except NotFoundException as e:
        raise HTTPException(status_code=409, detail=f"{e}")
    return Accessory(**result.__dict__)


@router.delete("/{item_id}")
async def delete_book(item_id: int, session: AsyncSession = Depends(get_session)):
    """Delete accessory by `id`"""
    repo = AccessoryRepo(session)
    await repo.delete(item_id)
    return Response(status_code=204)
