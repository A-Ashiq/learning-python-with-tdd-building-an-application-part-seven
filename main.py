from domain.taxes import calculate_income_tax_owed
from interfaces.api.main import app


@app.get(path="/income-taxes")
def calculate_income_taxes(salary: float) -> dict[str, float]:
    tax_owed: float = calculate_income_tax_owed(salary=salary)
    return {"tax owed": tax_owed}
