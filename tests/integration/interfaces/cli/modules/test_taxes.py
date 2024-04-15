from click.testing import Result
from typer.testing import CliRunner

from cli import app

runner = CliRunner()


class TestCalculateIncomeTaxed:
    def test_returns_correct_calculation(self):
        """
        Given a salary of £10,000
        When the `taxes calculate-income-taxes` command is called
        Then the correct calculation is returned in the standard output
        """
        # Given
        salary = 10_000
        main_module_name = "taxes"
        sub_module_name = "calculate-income-taxes"
        cli_runner = CliRunner()

        # When
        result: Result = cli_runner.invoke(app=app, args=[main_module_name, sub_module_name, str(salary)])

        # Then
        assert result.exit_code == 0
        assert "£0" in result.stdout
