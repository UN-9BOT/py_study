"""Overload operator."""
from __future__ import annotations


class Oper:
    """Left operand."""

    def __init__(self, n: int):
        """Init with 1 field."""
        self.n: int = n

    def __add__(self, other: Oper) -> Oper:
        """Overload +."""
        return Oper(self.n + other.n)


def main() -> None:
    """Func main."""
    a: Oper = Oper(4)
    b: Oper = Oper(5)

    print((a + b).n)


if __name__ == "__main__":
    main()
