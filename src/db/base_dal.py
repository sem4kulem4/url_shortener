from typing import Type, TypeVar

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.base_models import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseDAL:
    def __init__(self, model: Type[ModelType], db_session: AsyncSession):
        self._session_factory = db_session
        self.model = model

    async def get_single(self, **filters):
        async with self._session_factory() as session:
            row = await session.execute(select(self.model).filter_by(**filters))
            return row.scalar_one_or_none()

    async def create(self, **data):
        async with self._session_factory() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def delete(self, **filters):
        async with self._session_factory() as session:
            deleted = await session.execute(
                delete(self.model).filter_by(**filters).returning(self.model.id)
            )
            await session.commit()
            return deleted.scalars().fetchall()
