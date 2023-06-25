from sqlalchemy import delete, func, insert, select, update
from src.db import Session

from src.candies.models import Candies


class CandiesRepository:
    @classmethod
    def add(cls, values: dict):
        with Session() as session:
            stmt = insert(Candies).values(**values).returning(Candies)
            new_candy = session.execute(stmt)
            session.commit()
            return new_candy.scalar_one()
        
    @classmethod
    def get(cls, candy_id: int):
        query = select(Candies.__table__.columns).filter_by(id=candy_id)
        with Session() as session:
            candy = session.execute(query)
            session.commit()
            return candy.mappings().one()

    @classmethod
    def list(cls, filter_by: dict):
        query = select(Candies).filter_by(**filter_by)
        with Session() as session:
            candies = session.execute(query)
            session.commit()
            return candies.scalars().all()

    @classmethod
    def count(cls) -> int:
        query = select(func.count(Candies.id)).select_from(Candies)
        with Session() as session:
            candies_count = session.execute(query)
            session.commit()
            return candies_count.scalar()

    @classmethod
    def update(cls, candy_id: int, values: dict):
        stmt = update(Candies).where(Candies.id == candy_id).values(**values)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def finish(cls, candy_id: int, values: dict):
        stmt = update(Candies).where(Candies.id == candy_id).values(**values)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete(cls, candy_id: int):
        stmt = delete(Candies).where(Candies.id == candy_id)
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def delete_all(cls):
        stmt = delete(Candies)
        with Session() as session:
            session.execute(stmt)
            session.commit()
