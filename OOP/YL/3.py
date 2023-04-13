"""Ex3 2 class and polymorf."""
from secrets import randbelow
from time import sleep


class Unit:
    """Unit for all classes."""

    id: int = 0

    def __init__(self, party: str) -> None:
        """Init super."""
        self.party = party


class Hero(Unit):
    """Class for main unit."""

    def __init__(self, party: str) -> None:
        """Init and increment id."""
        super().__init__(party)
        Unit.id += 1
        self.__id: int = Unit.id
        self.__lvl = 0

    def lvlUp(self):
        """For lvl up."""
        self.__lvl += 1


class Soldier(Unit):
    """Class for soldiers."""

    def __init__(self, party: str) -> None:
        """Init and add to party."""
        super().__init__(party)
        self.__link: None | Hero = None

    def follow(self, target: Hero):
        """Func for follow to hero."""
        self.__link = target


def main() -> None:
    """Func main."""
    partys: list[str] = ["Goblins", "Kobolts", "Humans", "Orks"]
    heroes: list[Hero] = []
    soldiers: dict[str, list[Soldier]] = {p: [] for p in partys}

    print("Start generate heroes:")
    sleep(1)
    for n, p in enumerate(partys):
        sleep(1)
        print(f"Generate {n} hero- {p}")
        heroes.append(Hero(p))
    leader: Hero = heroes[0]
    for p in partys:
        sleep(1)
        for _ in range(randbelow(100)):
            soldiers[p].append(Soldier(p))
        print(f"Amount soldiers in {p}-party = {len(soldiers[p])}")
        if len(soldiers[p]) > len(soldiers[leader.party]):
            leader = next((h for h in heroes if h.party == p))
    print(f"Leader - {leader.party}")

    soldiers[partys[0]][0].follow(heroes[0])
    print(f"Soldier - {id(soldiers[partys[0]][0])} follow to {id(heroes[0])}")


if __name__ == "__main__":
    main()
