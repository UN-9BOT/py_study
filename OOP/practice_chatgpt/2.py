"""Factorial calculator."""
from __future__ import annotations


class FactorialCalculator:
    """Basic class without objects."""

    @staticmethod
    def check_except(num: int) -> None:
        """For checking num."""
        if num <= 0:
            raise ValueError("Number should be a positive")

    @staticmethod
    def calculate(num: int) -> int:
        """Func main."""
        FactorialCalculator.check_except(num)
        if num == 1:
            return 1
        return num * FactorialCalculator.calculate(num - 1)


print(FactorialCalculator.calculate(5))
