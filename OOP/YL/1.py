"""Ex1 warriors and random hit."""

from __future__ import annotations
from time import sleep
from secrets import randbelow


class Warrior:
    """Class for units."""

    def __init__(self, name: str) -> None:
        """Init module."""
        self.health: int = 100
        self.hitdmg: int = 20
        self.name: str = name

    def hit(self, other: Warrior):
        """Func for hit other unit."""
        other.health -= self.hitdmg


def main() -> None:
    """Func start fight."""
    units: list[Warrior] = [Warrior("Olaf"), Warrior("Domy")]

    while all(i.health > 0 for i in units):
        attacker: Warrior = units[randbelow(2)]
        deffender: Warrior = units[randbelow(2)]

        if attacker is not deffender:
            attacker.hit(deffender)
            print(f"{attacker.name} hit -> {deffender.name}.")
            print(f"\t{units[0].name} ({units[0].health})")
            print(f"\t{units[1].name} ({units[1].health})")
            sleep(1)

    winner: str = units[0].name if units[0].health > 0 else units[1].name
    print(f"Winner is {winner}")


if __name__ == "__main__":
    main()
