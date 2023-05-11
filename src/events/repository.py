
class EventsDB:
    @classmethod
    def add(
        cls,
        title,
        date,
        location,
        price,
        tickets,
    ):
        query = insert(Events).values(
            title=title,
            date=date,
            location=location,
            price=price,
            tickets=tickets,
        ).returning(Events.id)
    
        with Session() as session:
            event = session.execute(query)
            session.commit()
            return event.one()
            