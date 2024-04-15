from typer import Typer

from domain.taxes import calculate_income_tax_owed

app = Typer()


@app.command()
def calculate_income_taxes(salary: float) -> None:
    calculated_tax: float = calculate_income_tax_owed(salary=salary)
    print(f"£{calculated_tax}")
