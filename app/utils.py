from datetime import datetime

from sqlmodel import Session
from fastapi import Request
from database import engine


# global functions that jinja templates can access
# send flash messages to the alert area during redirect
def flash(request: Request, message: str, category: str = "primary") -> None:
    if "_messages" not in request.session:
        request.session["_messages"] = []
    request.session["_messages"].append({"message": message, "category": category})


def get_flashed_messages(request: Request) -> list[str]:
    return request.session.pop("_messages") if "_messages" in request.session else []


def get_session():
    with Session(engine) as session:
        yield session


def validate_datetime(date: str) -> datetime | None:
    """Convers html datetime-local form format to postgresql datetime format
    Empty datetime strings, which show as 'mm/dd/yy 00:00' in the form,
    will be returned as 'None'
    """
    try:
        validated_datetime = datetime.strptime(date, "%Y-%m-%dT%H:%M")
        return validated_datetime
    except (ValueError):
        return None


def format_time(date: datetime) -> str | None:
    """Converts Python datetime object to string format in order for the
    datetime-local input box to recognize properly."""
    try:
        return date.strftime("%Y-%m-%dT%H:%M")
    except (AttributeError):
        return None
