import time


def execution_time(func):

    def wrapper(

        *args,

        **kwargs

    ):

        start = time.time()

        result = func(

            *args,

            **kwargs

        )

        print(

            f"{func.__name__} : "

            f"{time.time()-start:.4f} sec"

        )

        return result

    return wrapper