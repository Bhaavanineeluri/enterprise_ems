import redis

from core.config import settings


redis_client = redis.Redis(

    host=settings.REDIS_HOST,

    port=settings.REDIS_PORT,

    decode_responses=True

)


def get_cache(key: str):

    return redis_client.get(key)


def set_cache(

    key: str,

    value,

    expire: int = 300

):

    redis_client.set(

        key,

        value,

        ex=expire

    )


def delete_cache(key: str):

    redis_client.delete(key)