import functools
import typing


class App:
    def __init__(self):
        self.on_startup: typing.Callable
        self.on_shutdown: typing.Callable

    def startup(self):
        def wrapper(func: typing.Callable):
            self.on_startup = func

        return wrapper

    def shutdown(self):
        def wrapper(func: typing.Callable):
            self.on_shutdown = func

        return wrapper

    def run(self):
        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                await self.on_startup()
                await func(*args, **kwargs)
                await self.on_shutdown()

            return wrapped

        return wrapper
