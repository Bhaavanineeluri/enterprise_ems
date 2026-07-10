import time

from fastapi import HTTPException


requests = {}


def rate_limit(

    key: str,

    limit: int = 100,

    window: int = 60

):

    now = time.time()

    history = requests.get(key, [])

    history = [

        t for t in history

        if now - t < window

    ]

    if len(history) >= limit:

        raise HTTPException(

            status_code=429,

            detail="Too many requests"

        )

    history.append(now)

    requests[key] = history