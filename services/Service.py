from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    update, delete
)
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import (
    create_async_engine, AsyncSession
)

from models.Base import Base

url_do_banco = 'sqlite+aiosqlite:///db.db'

engine = create_async_engine(url_do_banco)

session = sessionmaker(
    engine,
    expire_on_commit=False,
    future=True,
    class_=AsyncSession,
)


class Service:

    @staticmethod
    async def create_database():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def create(entity, payload):
        async with session() as s:
            entity_created = entity(payload)
            s.add(entity_created)
            await s.commit()
            return entity_created

    @staticmethod
    async def search(entity, attr, value):
        async with session() as s:
            query = await s.execute(
                select(entity).where(getattr(entity, attr) == value)
            )
            return query.scalars().all()

    @staticmethod
    async def update(entity, attr, value, old_value):
        async with session() as s:
            await s.execute(
                update(entity).where(
                    getattr(entity, attr) == old_value
                ).values({attr: value})
            )
            await s.commit()

    @staticmethod
    async def delete(entity, attr, value):
        async with session() as s:
            await s.execute(
                delete(entity).where(
                    getattr(entity, attr) == value
                )
            )
            await s.commit()

    @staticmethod
    async def join_search(entity, join_entity, attr, join_attr, value):
        async with session() as s:
            query = await s.execute(
                select(entity, join_entity).join(
                    getattr(join_entity, join_attr)
                ).where(
                    getattr(entity, attr) == value
                )
            )
            return query.scalars().all()
