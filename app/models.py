from typing import Annotated, Optional

from fastapi import Form
from sqlmodel import Field, SQLModel


class DailyTasks(SQLModel, table=True):
    ROWID: Optional[int] = Field(default=None, primary_key=True)
    date: Annotated[str, Form(...)]
    calories: Annotated[int, Form(...)]
    gym: Annotated[bool | None, Form()] = False
    language: Annotated[bool | None, Form()] = False
    coding: Annotated[bool | None, Form()] = False
    music: Annotated[bool | None, Form()] = False
    other: Annotated[str | None, Form()] = ""
