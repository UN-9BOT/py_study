"""Encapsulation. Set atr, dict. __."""
from typing import Union


class Hide:
    """
    Hiden class.

    All atributes hiden. All work with methods. Overload.

    """

    __slots__ = ["new_a", "__id"]

    __countObj: int = 0

    def __init__(self, id: int) -> None:
        """Init module with __var."""
        Hide.__countObj += 1
        self.__setattr__("_Hide__id", id, 1)

    def __setattr__(self, name: str, value: int, allow_atr: int = 0) -> None:
        """Overload setting atribut."""
        if hasattr(Hide, name) and allow_atr:
            super().__setattr__(name, value)
        else:
            raise AttributeError

    def __getattribute__(self, name, allow_access=0):
        """Overload get atr."""
        if allow_access:
            return super().__getattribute__(name)
        else:
            raise PermissionError(
                "Access denied. The attribute value can \
                        only be retrieved using the 'get_atr' method."
            )

    def set_atr(self, name: str, value: int) -> None:
        """Set atr with check type."""
        if type(value) == int:
            self.__setattr__(name, value, 1)
        else:
            raise TypeError("Attribute value must be of type int")

    def get_atr(self, name: str) -> Union[int, None]:
        """Get atr."""
        res: Union[int, None] = None
        if hasattr(self, name):
            res = getattr(self, name)
        return res


def main() -> None:
    """Func main."""
    hide_obj: Hide = Hide(1)
    hide_obj.set_atr("new_a", 4)
    print(hide_obj.get_atr("new_a"))

    # all actions bottom raise exception
    # print(obj.new_a)
    # obj.set_atr("id", 2)
    # obj.new_a = 2


if __name__ == "__main__":
    main()
