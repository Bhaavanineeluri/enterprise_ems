from fastapi import Request
from fastapi.responses import JSONResponse

from core.exceptions.custom import AppException

from utils.response import error_response




async def app_exception_handler(
    request: Request,
    exc: AppException
):

    return JSONResponse(

        status_code=exc.status_code,

        content=error_response(

            message=exc.message,

            status_code=exc.status_code

        )

    )




async def global_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(

        status_code=500,

        content=error_response(

            message="Internal server error",

            status_code=500

        )

    )