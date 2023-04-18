"""Basic calculator without objects."""
from __future__ import annotations


class Calculator:
    """Realize calculator with 4 operators and 2 operands."""

    last_res: float = 0.0

    @classmethod
    def add(cls, num1: float, num2: float) -> float:
        """Add 2 nums."""
        cls.last_res = num1 + num2
        return cls.last_res

    @classmethod
    def sub(cls, num1: float, num2: float) -> float:
        """Substract 2 nums."""
        cls.last_res = num1 - num2
        return cls.last_res

    @classmethod
    def mul(cls, num1: float, num2: float) -> float:
        """Multiply 2 nums."""
        cls.last_res = num1 * num2
        return cls.last_res

    @classmethod
    def div(cls, num1: float, num2: float) -> float:
        """Division 2 nums."""
        if num2 == 0:
            raise ZeroDivisionError("Division by zero")
        cls.last_res = num1 / num2
        return cls.last_res

    @classmethod
    def get_last_result(cls) -> float:
        """For getting last calculating result."""
        return cls.last_res
