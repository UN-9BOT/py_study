"""Realize generator-func witth random int nums. As ex 9."""
from secrets import randbelow
from pydantic import PositiveInt
from typing import Iterator


def rand_int_gen(count: PositiveInt, min_num: int,
                 max_num: int) -> Iterator[int]:
    """Func Generator."""
    if count <= 0:
        raise ValueError("Count must be a positive integer")
    if max_num <= min_num:
        raise ValueError("Max num must be greater than min number")
    while count > 0:
        yield randbelow(max_num - min_num + 1) + min_num
        count -= 1


def main() -> None:
    """Func main."""
    s = rand_int_gen(10, -5, 5)
    for i in s:
        print(i)


if __name__ == "__main__":
    main()
