import models
from sqlalchemy.orm import Session


def get_all_records(db: Session):
    return db.query(models.DailyTasks).all()


def get_all_todo_records(db: Session):
    return db.query(models.DailyTodo).all()


def get_record_by_rowid(db: Session, ROWID: int):
    return db.query(models.DailyTasks).filter(models.DailyTasks.ROWID == ROWID).first()


def get_record_by_date(db: Session, date: str):
    return db.query(models.DailyTasks).filter(models.DailyTasks.date == date).first()


def create_record(db: Session, record: models.DailyTasks):
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def update_record(db: Session, record: models.DailyTasks):
    db_record = db.get(models.DailyTasks, record.ROWID)
    print(record)
    record_dict = record.dict(exclude_unset=True)
    for k, v in record_dict.items():
        print(k, v)
        setattr(db_record, k, v)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
