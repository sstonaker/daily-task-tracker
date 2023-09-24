import crud
import utils
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

router = APIRouter()

templates = Jinja2Templates(directory="templates")
templates.env.globals["get_flashed_messages"] = utils.get_flashed_messages


@router.get("/")
def index(
    request: Request,
    db: Session = Depends(utils.get_db),
):
    try:
        daily_tasks = crud.get_all_records(db)
    except Exception as e:
        utils.flash(
            request, f"Unable to retrieve anomalies from database. {e}", "alert-danger"
        )
        return templates.TemplateResponse("error.html", {"request": request})

    return daily_tasks
