from unittest import mock

from cli import app
from click.testing import Result
from typer.testing import CliRunner

MODULE_PATH = "interfaces.cli.modules.taxes"


class TestCalculateIncomeTaxes:
    @mock.patch(f"{MODULE_PATH}.calculate_income_tax_owed")
    def test_delegates_call_to_domain_logic(
        self, spy_calculate_income_tax_owed: mock.MagicMock
    ):
        """
        Given a salary of £10,000
        When the `taxes calculate-income-taxes` command is called
        Then the call is delegated to `calculate_income_tax_owed()`
            to perform the calculation
        """
        # Given
        salary = 10_000
        cli_runner = CliRunner()

        # When
        result: Result = cli_runner.invoke(
            app=app, args=["taxes", "calculate-income-taxes", str(salary)]
        )

        # Then
        spy_calculate_income_tax_owed.assert_called_once_with(salary=salary)

        returned_calculation = spy_calculate_income_tax_owed.return_value
        assert f"£{returned_calculation}" in result.stdout
