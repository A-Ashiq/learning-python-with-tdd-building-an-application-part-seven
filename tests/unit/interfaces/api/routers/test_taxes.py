from unittest import mock

from starlette.testclient import TestClient

from interfaces.api.main import app


MODULE_PATH = "interfaces.api.routers.taxes"


class TestCalculateIncomeTaxes:
    @mock.patch(f"{MODULE_PATH}.calculate_income_tax_owed")
    def test_delegates_call_to_domain_logic(
        self, spy_calculate_income_tax_owed: mock.MagicMock
    ):
        """
        Given a salary of £10,000
        When a GET request is made to the `income-taxes/` endpoint
        Then the call is delegated to `calculate_income_tax_owed()`
            to perform the calculation
        """
        # Given
        test_client = TestClient(app=app)
        salary = 10_000
        spy_calculate_income_tax_owed.return_value = 123

        # When
        response = test_client.get("/income-taxes", params={"salary": salary})

        # Then
        spy_calculate_income_tax_owed.assert_called_once_with(salary=salary)

        returned_calculation = spy_calculate_income_tax_owed.return_value
        assert response.json() == {"tax owed": returned_calculation}
