"""Module for working parsing file."""
from time import time
from typing import Any, Callable


def measure_time(func: Callable[..., Any]) -> Callable[..., list[str]]:
    """Decorate for measure time function execution."""

    def inner(*args, **kwargs) -> list[str]:
        """Inner func."""
        start: float = time()
        res_func: list[str] = func(*args, **kwargs)
        res: float = time() - start
        print(f"{measure_time.__name__} took {res} seconds to run.")
        return res_func

    return inner


class FileParser:
    """For work with File. Allows read file, parse word, count word."""

    def __init__(self, path: str) -> None:
        """Overload constructor."""
        self.path: str = path

    @measure_time
    def parse_file(self) -> list[str]:
        """For parsing file in path."""
        lst: list[str] = []
        try:
            with open(self.path, "r") as f:
                for line in f:
                    if not line.startswith("#") and line != '\n':
                        lst.append(line.removesuffix('\n'))
        except FileNotFoundError:
            print("File not found error")
        except Exception as e:
            print(f"Exception {e}")
        return lst

    @staticmethod
    @measure_time
    def get_words_count(lst: list[str]) -> dict[str, int]:
        """For counting word in list strings. Without registr alpha."""
        res: dict[str, int] = {}
        for line in lst:
            words: list[str] = line.split()
            for word in words:
                if word.lower() not in res:
                    res[word.lower()] = 1
                else:
                    res[word.lower()] += 1
        return res


def main() -> None:
    """Test func."""
    fp: FileParser = FileParser("data_5.txt")

    res: list[str] = fp.parse_file()
    print(res)
    print(fp.get_words_count(res))


if __name__ == "__main__":
    main()
