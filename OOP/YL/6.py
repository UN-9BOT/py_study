"""Ex 6. Calculate room."""
from typing import Union
from math import ceil


class WinDoor:
    """
    Associate 2 object.

    For 2 objects: window and door. Objects need only 1 field - square.
    """

    def __init__(self, h: int, w: int) -> None:
        """Overload func for init with 1 field."""
        self.square: int = h * w


class Room:
    """Main class."""

    def __init__(
        self, x: Union[int, float], y: Union[int, float], z: Union[int, float]
    ) -> None:
        """Overload func for init."""
        self.widht: Union[int, float] = x
        self.lenght: Union[int, float] = y
        self.height: Union[int, float] = z
        self.wd: list[WinDoor] = []

    def add_wd(self, w: int, h: int) -> None:
        """Func for create 1 obj - type WinDoor."""
        self.wd.append(WinDoor(h, w))

    def work_surface(self) -> Union[float, int]:
        """Finite calculating."""
        square: Union[float, int] = 2 * self.height * (
                self.widht + self.lenght)
        for i in self.wd:
            square -= i.square
        return square

    @staticmethod
    def get_roll(square: Union[int, float],
                 height: Union[int, float],
                 lenght: Union[int, float]) -> int:
        """Return count rolls for defined area."""
        return ceil(square / (height * lenght))


def main() -> None:
    """Func main calculating."""
    room = Room(6, 3, 2.7)
    room.add_wd(1, 1)
    room.add_wd(1, 1)
    room.add_wd(1, 2)
    print(room.work_surface())
    print(Room.get_roll(room.work_surface(), 1, 3.2))


if __name__ == "__main__":
    main()
