from http import HTTPStatus

from starlette.testclient import TestClient

from main import app, calculate_income_tax_owed

import pytest


class TestIncomeTaxesEndpoint:
    def test_calculates_correct_tax(self):
        """
        Given a salary of £33,000
        When a GET request is made to the `income-taxes/` endpoint
        Then the calculated tax owed is £4,086
        """
        # Given
        test_client = TestClient(app=app)
        salary = 33_000

        # When
        response = test_client.get("/income-taxes", params={"salary": salary})

        # Then
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"tax owed": 4_086}


...


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
