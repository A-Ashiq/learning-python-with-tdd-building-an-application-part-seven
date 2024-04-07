from fastapi import FastAPI

app = FastAPI()


@app.get(path="/income-taxes")
def calculate_income_taxes(salary: float) -> dict[str, float]:
    tax_free_allowance = 12_570
    tax_owed = (salary - tax_free_allowance) * 0.2

    return {"tax owed": tax_owed}
