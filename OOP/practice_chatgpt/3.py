"""Simple project for work with files and classes."""
import json
from typing import Optional


class User:
    """For all units."""

    def __init__(self, name: Optional[str], age: int) -> None:
        """Overload constructor with 2 field."""
        self.name: Optional[str] = name
        self.age: int = age


class File:
    """For work with file read/write."""

    @classmethod
    def write(cls, unit: User) -> None:
        """For append in data in bin format."""
        with open("users.json", "a") as f:
            user_dict = {"name": unit.name, "age": unit.age}
            json.dump(user_dict, f)
            f.write('\n')

    @classmethod
    def find_user(cls, name: str) -> Optional[User]:
        """For search user by name."""
        try:
            with open("users.json", "r") as f:
                for line in f:
                    user: dict[str, str] = json.loads(line)
                    if user.get("name") == name:
                        return User(user["name"], int(user["age"]))
        except FileNotFoundError:
            return None
        return None


def main() -> None:
    """Func main."""
    for i in range(10):
        File.write(User(str(i), i))

    f_user: Optional[User] = File.find_user("4")
    if f_user is not None:
        print(f_user.age)


if __name__ == "__main__":
    main()
