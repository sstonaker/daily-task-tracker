import models
from sqlalchemy.orm import Session


def get_all_records(db: Session):
    return db.query(models.DailyTask).all()
