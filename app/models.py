from sqlmodel import Field, SQLModel
from fastapi import Form
from typing import Annotated


class DailyTasks(SQLModel, table=True):
    ROWID: int | None = Field(default=None, primary_key=True)
    date: Annotated[str, Form()]
    calories: Annotated[int, Form()]
    gym: Annotated[bool | None, Form()] = False
    language: Annotated[bool | None, Form()] = False
    coding: Annotated[bool | None, Form()] = False
    music: Annotated[bool | None, Form()] = False
    other: Annotated[str | None, Form()] = ""


class DailyTodo(SQLModel, table=True):
    ROWID: int | None = Field(default=None, primary_key=True)
    date: Annotated[str, Form()]
    todo: Annotated[str | None, Form()] = ""
    done: Annotated[bool | None, Form()] = False
