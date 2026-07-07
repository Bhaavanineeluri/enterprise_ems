from fastapi import APIRouter
from fastapi import BackgroundTasks

from services.background import (

    email_task,

    sms_task

)


router = APIRouter(

    prefix="/background",

    tags=["Background"]

)


@router.post("/email")
def queue_email(

    email: str,

    background_tasks: BackgroundTasks

):

    return email_task(

        background_tasks,

        email

    )


@router.post("/sms")
def queue_sms(

    phone: str,

    background_tasks: BackgroundTasks

):

    return sms_task(

        background_tasks,

        phone

    )
@router.post("/batch")
def batch(

    items: list[str]

):

    from services.background import process_batch

    return process_batch(items)