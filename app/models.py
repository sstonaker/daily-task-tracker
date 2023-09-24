
from database import Base
from sqlalchemy import Boolean, Column, Date, Integer, Text


class DailyTask(Base):
    __tablename__ = "daily_tasks"

    ROWID = Column(Integer, primary_key=True)
    date = Column(Text)
    calories = Column(Integer)
    gym = Column(Boolean)
    language = Column(Boolean)
    coding = Column(Boolean)
    music = Column(Boolean)
    other = Column(Text)
