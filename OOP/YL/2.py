"""This module for 2 ex."""
from secrets import randbelow


class Person:
    """Class for units."""

    def __init__(self, name: str, sname: str, lvl: int = 1) -> None:
        """Init module with private vars."""
        self.__name: str = name
        self.__sname: str = sname
        self.__lvl: int = lvl

    def __del__(self) -> None:
        """For del 1 unit."""
        print(f"Goodbye {self.__name} {self.__sname} {self.__lvl}")
        del self

    def getInfo(self) -> str:
        """Get info."""
        return f"{self.__name}, {self.__sname}, {self.__lvl}"

    def getLvl(self) -> int:
        """Get lvl for 1 unit."""
        return self.__lvl


def main() -> None:
    """Func for start."""
    units: list[Person] = [
        Person("Olaf", "Berkley", randbelow(5)),
        Person("Beely", "Switherman", randbelow(5)),
        Person("Kelly", "Leinman", randbelow(5)),
    ]

    lowUn: Person = units[0]
    for un in units:
        if un.getLvl() < lowUn.getLvl():
            lowUn = un

    print(f"Слабое звено - {lowUn.getInfo()}")
    lowUn.__del__()


if __name__ == "__main__":
    main()
