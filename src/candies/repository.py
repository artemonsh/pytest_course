from sqlalchemy import delete, func, insert, literal_column, select, update
from db import Session

from candies.models import Candies
from candies.api import Candy


class CandiesDB:
    # @classmethod
    # def add(cls, candy: Candy):
    #     with Session() as session:
    #         stmt = insert(Candies).values(**candy.to_dict_wo_id()).returning(Candies.id)
    #         candy = session.execute(stmt)
    #         session.commit()
    #         candy = candy.scalar_one()
    #     return Candy.from_orm(candy)
    
    @classmethod
    def add(cls, candy: Candy):
        with Session() as session:
            stmt = insert(Candies).values(**candy.to_dict_wo_id()).returning(Candies)
            new_candy = session.execute(stmt)
            session.commit()
            new_candy = new_candy.mappings().one()["Candies"]
        return Candy.from_orm(new_candy)
        
    @classmethod
    def get(cls, candy_id: int):
        query = select(Candies.__table__.columns).filter_by(id=candy_id)
        with Session() as session:
            candy = session.execute(query)
            session.commit()
            candy = candy.mappings().one()
        return Candy.from_dict(candy)

    @classmethod
    def list(cls, location=None, price=0):
        filter_by = {}
        if location:
            filter_by |= {"location": location}
        if price:
            filter_by |= {"price": price}
        query = select(Candies).filter_by(**filter_by)
        with Session() as session:
            candies = session.execute(query)
            session.commit()
            candy = candies.mappings().all()
        return Candy.from_dict(candy)

    @classmethod
    def count(cls) -> int:
        query = select(func.count(Candies.id)).select_from(Candies)
        with Session() as session:
            candies_count = session.execute(query)
            session.commit()
        return candies_count.scalar()

    @classmethod
    def update(cls, candy_id: int, candy: Candy):
        stmt = update(Candies).where(Candies.id == candy_id).values(**candy.to_dict_wo_id())
        with Session() as session:
            session.execute(stmt)
            session.commit()

    @classmethod
    def finish(cls, candy_id: int):
        stmt = update(Candies).where(Candies.id == candy_id).values(is_passed=True)
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
