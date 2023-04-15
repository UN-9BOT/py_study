"""Realize iterator with random int nums."""
from __future__ import annotations
from secrets import randbelow
from pydantic import PositiveInt


class RandomIntIterator:
    """For iterator."""

    def __init__(self, count: int, min_num: int, max_num: int) -> None:
        """Overload constructor."""
        if count <= 0:
            raise ValueError("Count must be a positive integer")
        if max_num <= min_num:
            raise ValueError("Max num must be greater than min number")
        self.count: PositiveInt = count
        self.min_num: int = min_num
        self.max_num: int = max_num
        self.range_: int = max_num - min_num

    def __iter__(self) -> RandomIntIterator:
        """Overload for iterator object."""
        return self

    def __next__(self) -> int:
        """Generate list with random nums."""
        if not self.count:
            raise StopIteration
        self.count -= 1
        return randbelow(self.range_) + self.min_num


def main() -> None:
    """Func main."""
    rand_obj = RandomIntIterator(10, -10, 10)
    for i in rand_obj:
        print(i)


if __name__ == "__main__":
    main()
