from datetime import date

from pydantic import BaseModel


class DailyTask(BaseModel):
    ROWID: int
    date: str
    calories: int
    gym: bool
    language: bool
    coding: bool
    music: bool
    other: str

    class Config:
        orm_mode = True
