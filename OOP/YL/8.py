"""Ex 8."""
from math import pi


class Cylinder:
    """Main class with all methods."""

    __slots__ = ["di", "hi", "area"]

    @staticmethod
    def make_area(d, h):
        """For calculate value area."""
        circle = pi * d**2 / 4
        side = pi * d * h
        return round(circle * 2 + side, 2)

    def __init__(self, di, hi):
        """Overload constructor."""
        self.di = di
        self.hi = hi
        self.area = Cylinder.make_area(di, hi)

    def __setattr__(self, name: str, value: int):
        """
        Overload.

        Every setting new atribute or change old attribute recalculate area.
        """
        if name in self.__slots__:
            super().__setattr__(name, value)
            try:
                hi: int = self.__getattribute__("hi")
                di: int = self.__getattribute__("di")
                super().__setattr__("area", Cylinder.make_area(di, hi))
            except AttributeError:
                super().__setattr__("area", 0)
        else:
            raise AttributeError("Attribute not in __slots__")


def main() -> None:
    """Func main."""
    cyl_obj = Cylinder(1, 2)
    print(cyl_obj.area)
    cyl_obj.di = 2
    cyl_obj.area = 7  # not work, because overload func set
    print(cyl_obj.area)
    # print(cyl_obj.make_area(2, 2))


if __name__ == "__main__":
    main()
