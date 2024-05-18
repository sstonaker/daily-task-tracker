import crud
import models
import utils
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

router = APIRouter()

templates = Jinja2Templates(directory="templates")
templates.env.globals["get_flashed_messages"] = utils.get_flashed_messages


@router.get("/")
def index(
    request: Request,
    db: Session = Depends(utils.get_session),
):
    try:
        daily_tasks = crud.get_all_records(db)
    except Exception as e:
        utils.flash(
            request, f"Unable to retrieve records from database. {e}", "alert-danger"
        )
        return templates.TemplateResponse("error.html", {"request": request})

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "daily_tasks": daily_tasks,
        },
    )


@router.get("/record/{ROWID}")
def read(
    request: Request,
    ROWID: int,
    db: Session = Depends(utils.get_session),
):
    try:
        record = crud.get_record_by_rowid(db, ROWID)
    except TypeError as e:
        raise HTTPException(
            status_code=400, detail=f"Invalid id - must be integer-like. {e}"
        )
    if not record:
        raise HTTPException(
            status_code=502, detail=f"Record (id:{ROWID}) not found."
        )

    return templates.TemplateResponse(
        "task.html",
        {
            "request": request,
            "record": record,
        },
    )


@router.get("/record")
def add_record(
    request: Request
):
    return templates.TemplateResponse(
        "task.html",
        {
            "request": request
        },
    )


@router.post("/record")
def create(
    request: Request,
    form_data: models.DailyTasks = Depends(),
    db: Session = Depends(utils.get_session),
):
    existing_record = crud.get_record_by_date(db, form_data.date)

    if not existing_record:

        try:
            crud.create_record(db, form_data)
        except Exception as e:
            raise HTTPException(
                status_code=502, detail=f"Unable to add record. {e}"
            )

        utils.flash(
            request, "New record added.", "alert-success"
        )
    else:
        utils.flash(
            request, "Date already exists.", "alert-danger"
        )

    # status code must be changed since by default redirect (307) preserves the
    # request type - index as "GET" will not accept redirect with "POST" from this route
    return RedirectResponse(
        url=request.url_for("index"), status_code=status.HTTP_303_SEE_OTHER
    )


@router.post("/record/{ROWID}")
async def update(
    request: Request,
    form_data: models.DailyTasks = Depends(),
    db: Session = Depends(utils.get_session),
):
    try:
        crud.update_record(db, form_data)
    except Exception as e:
        raise HTTPException(
            status_code=502, detail=f"Unable to add record. {e}"
        )

    utils.flash(
        request, "Record updated.", "alert-success"
    )

    # status code must be changed since by default redirect (307) preserves the
    # request type - index as "GET" will not accept redirect with "POST" from this route
    return RedirectResponse(
        url=request.url_for("index"), status_code=status.HTTP_303_SEE_OTHER
    )


@router.get("/todo")
def todo(
    request: Request,
    db: Session = Depends(utils.get_session),
):
    try:
        todo = crud.get_all_todo_records(db)
    except Exception as e:
        utils.flash(
            request, f"Unable to retrieve records from database. {e}", "alert-danger"
        )
        return templates.TemplateResponse("error.html", {"request": request})

    return templates.TemplateResponse(
        "todo.html",
        {
            "request": request,
            "todo": todo,
        },
    )


@router.get("/todo/record")
def add_task(
    request: Request
):
    return templates.TemplateResponse(
        "todotask.html",
        {
            "request": request
        },
    )


@router.post("/todo/record")
def todo_create(
    request: Request,
    form_data: models.DailyTodo = Depends(),
    db: Session = Depends(utils.get_session),
):

    try:
        crud.create_todo_record(db, form_data)
    except Exception as e:
        raise HTTPException(
            status_code=502, detail=f"Unable to add record. {e}"
        )

    utils.flash(
        request, "New record added.", "alert-success"
    )

    # status code must be changed since by default redirect (307) preserves the
    # request type - index as "GET" will not accept redirect with "POST" from this route
    return RedirectResponse(
        url=request.url_for("todo"), status_code=status.HTTP_303_SEE_OTHER
    )


@router.post("/todo/record/{ROWID}")
async def todo_update(
    request: Request,
    form_data: models.DailyTodo = Depends(),
    db: Session = Depends(utils.get_session),
):
    try:
        crud.update_todo_record(db, form_data)
    except Exception as e:
        raise HTTPException(
            status_code=502, detail=f"Unable to add record. {e}"
        )

    utils.flash(
        request, "Record updated.", "alert-success"
    )

    # status code must be changed since by default redirect (307) preserves the
    # request type - index as "GET" will not accept redirect with "POST" from this route
    return RedirectResponse(
        url=request.url_for("todo"), status_code=status.HTTP_303_SEE_OTHER
    )


@router.get("/todo/record/{ROWID}")
def read_todo(
    request: Request,
    ROWID: int,
    db: Session = Depends(utils.get_session),
):
    try:
        record = crud.get_todo_record_by_rowid(db, ROWID)
    except TypeError as e:
        raise HTTPException(
            status_code=400, detail=f"Invalid id - must be integer-like. {e}"
        )
    if not record:
        raise HTTPException(
            status_code=502, detail=f"Record (id:{ROWID}) not found."
        )

    return templates.TemplateResponse(
        "todotask.html",
        {
            "request": request,
            "record": record,
        },
    )
