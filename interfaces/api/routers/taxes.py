from fastapi import APIRouter

from domain.taxes import calculate_income_tax_owed

router = APIRouter()


@router.get(path="/income-taxes")
def calculate_income_taxes(salary: float) -> dict[str, float]:
    tax_owed: float = calculate_income_tax_owed(salary=salary)
    return {"tax owed": tax_owed}
