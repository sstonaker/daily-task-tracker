from sqlmodel import SQLModel, create_engine

SQLITE_URL = (
    "sqlite:///daily-task-tracker.db"
)
engine = create_engine(SQLITE_URL, echo=True)
SQLModel.metadata.create_all(engine)
