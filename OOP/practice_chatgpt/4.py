"""Basic decorator for measure time function execution."""
from time import time, sleep
from typing import Any, Callable


class Decorator:
    """Decorate with class."""

    def __init__(self, func: Callable[..., None]) -> None:
        """Overload constuctor."""
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> None:
        """Overload callable func."""
        start: float = time()
        self.func(*args, **kwds)
        res: float = time() - start
        print(f"{self.func.__name__} took {res} seconds to run.")


def measure_time(func: Callable[..., None]) -> Callable[..., None]:
    """Decorate for measure time function execution."""

    def inner(*args, **kwargs) -> None:
        """Inner func."""
        start: float = time()
        func(*args, **kwargs)
        res: float = time() - start
        print(f"{measure_time.__name__} took {res} seconds to run.")

    return inner


@Decorator
def test_func() -> None:
    """Testing func."""
    sleep(1)


if __name__ == "__main__":
    test_func()
