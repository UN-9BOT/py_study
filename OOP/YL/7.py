"""Printer 'snow' with Overload standart math operands."""


class Snow:
    """Main class with all overloading func's."""

    def __init__(self, countSnow) -> None:
        """Overload constructor class."""
        self.countSnow: int = countSnow

    def __add__(self, num: int) -> None:
        """Add 'num' snow in countSnow object."""
        self.countSnow += num

    def __sub__(self, num: int) -> None:
        """Sub 'num' snow in countSnow object."""
        self.countSnow -= num

    def __mul__(self, num: int) -> None:
        """Mul 'num' snow in countSnow object."""
        self.countSnow *= num

    def __truediv__(self, num: int) -> None:
        """Integer division 'num' snow in countSnow object."""
        self.countSnow //= num

    def makeSnow(self, cols: int) -> str:
        """Make snow."""
        res: str = ("*" * cols + "\n") * (self.countSnow // cols)
        return res


def main() -> None:
    """Func main."""
    snow_obj = Snow(5)
    snow_obj * 2
    snow_obj + 10
    print(snow_obj.makeSnow(5))


if __name__ == "__main__":
    main()
