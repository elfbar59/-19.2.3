import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):


        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.division(self, 2, 2) == 4

