"""Decorator on class."""
from typing import Any, Callable
from time import time, sleep


class Decorator:
    """Basic decorator."""

    def __init__(self, func: Callable[..., Any]) -> None:
        """Overload constructor."""
        self.func: Callable[..., Any] = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Overload callable func."""
        start: float = time()
        self.func(*args, **kwds)
        res: float = time() - start
        print(f"{self.func.__name__} took {res} seconds to run")


@Decorator
def main() -> None:
    """Func main."""
    sleep(1)


if __name__ == "__main__":
    main()
