import requests


def send_webhook(

    url: str,

    payload: dict

):

    try:

        response = requests.post(

            url,

            json=payload,

            timeout=5

        )

        return response.status_code

    except Exception:

        return None