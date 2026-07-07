from datetime import datetime, UTC



def success_response(
    data=None,
    message="Success"
):

    return {

        "success": True,

        "message": message,

        "data": data,

        "timestamp":
            datetime.now(UTC)

    }




def error_response(
    message,
    status_code
):

    return {

        "success": False,

        "message": message,

        "status_code": status_code,

        "timestamp":
            datetime.now(UTC)

    }