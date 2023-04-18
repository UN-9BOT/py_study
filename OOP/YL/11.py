"""Virtual mini-model learning. Realize singleton pattern."""
from __future__ import annotations
from typing import Dict, Tuple, Type
from secrets import randbelow


class Data:
    """Singleton. Inside all data."""

    _instances: Dict[Type[Data], Data] = {}

    def __new__(cls, *args: str) -> Data:
        """
        Overload for check count instance.

        If instances 0. Then create single obj. Other return already created.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    def __init__(self, *args: Tuple[str, ...]) -> None:
        """Overload consructor."""
        self.lst: list[str] = list(*args)

    def __getitem__(self, num: int) -> str:
        """Overload, for get item by index."""
        return self.lst[num]


class Teacher:
    """For engagement with teachers."""

    def __init__(self) -> None:
        """Overload with 1 atr. Work - count of work."""
        self.work = 0

    def teach(self, info: str, *pupil: Pupil) -> None:
        """Func for teach some pupil a single piece of knowledge(info)."""
        for i in pupil:
            i.take(info)


class Pupil:
    """For kids."""

    def __init__(self) -> None:
        """Overload."""
        self.knowledges: list[str] = []

    def take(self, info: str) -> None:
        """For append knowledge list in object."""
        self.knowledges.append(info)

    def self_study(self, info: str):
        """Self-study for kids. Just append."""
        self.knowledges.append(info)

    def forget_something(self) -> None:
        """For forget something knowledge."""
        choice: int = randbelow(len(self.knowledges))
        self.knowledges.pop(choice)


def main() -> None:
    """Func main."""
    data1: Data = Data(("OOP", "SQL", "Python", "Java", "Linux"))
    vasya: Pupil = Pupil()
    petya: Pupil = Pupil()
    teacher = Teacher()
    teacher.teach(data1[2], vasya, petya)
    teacher.teach(data1[1], vasya, petya)
    petya.self_study(data1[3])
    petya.self_study(data1[4])
    print(petya.knowledges)
    petya.forget_something()
    print(petya.knowledges)


if __name__ == "__main__":
    main()
