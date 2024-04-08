import pytest

from domain.taxes import calculate_income_tax_owed


class TestCalculateIncomeTaxOwed:
    @pytest.mark.parametrize(
        "salary, expected_tax_owed",
        (
            [60_000, 11_432],
            [65_000, 13_432],
        ),
    )
    def test_calculates_for_higher_rate_banding(
        self, salary: int, expected_tax_owed: float
    ):
        """
        Given a salary which is in the higher rate banding
        When `calculate_income_tax_owed()` is called
        Then the correct calculated tax owed is returned
        """
        # Given
        input_salary = salary

        # When
        calculated_tax_owed: float = calculate_income_tax_owed(salary=input_salary)

        # Then
        assert calculated_tax_owed == expected_tax_owed

    @pytest.mark.parametrize(
        "salary",
        (0, 10, 100, 200, 1_000, 5_000, 12_568, 12_569),
    )
    def test_calculates_no_tax_when_salary_is_lower_than_personal_allowance(
        self, salary: int
    ):
        """
        Given a salary which lower than the personal allowance
        When `calculate_income_tax_owed()` is called
        Then the correct calculated tax owed of 0 is returned
        """
        # Given
        input_salary = salary

        # When
        calculated_tax_owed: int = calculate_income_tax_owed(salary=input_salary)

        # Then
        assert calculated_tax_owed == 0
