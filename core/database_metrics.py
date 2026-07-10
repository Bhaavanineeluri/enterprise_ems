from sqlalchemy.orm import Session


def count_rows(

    db: Session,

    model

):

    return db.query(

        model

    ).count()