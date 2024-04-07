from fastapi import FastAPI

app = FastAPI()


@app.get(path="/income-taxes")
def calculate_income_taxes(salary: float) -> dict[str, float]:
    tax_owed: float = calculate_income_tax_owed(salary=salary)
    return {"tax owed": tax_owed}


def calculate_income_tax_owed(salary: float) -> float:
    tax_free_allowance = 12_570
    return (salary - tax_free_allowance) * 0.2
