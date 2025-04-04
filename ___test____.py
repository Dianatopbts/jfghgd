import pytest
from app.calculator import Calculator

setup_method
teardown_method


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiple_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 4, 2) == 6