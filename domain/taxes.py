PERSONAL_ALLOWANCE_THRESHOLD = 12_570
HIGHER_RATE_THRESHOLD = 50_270
ADDITIONAL_RATE_THRESHOLD = 125_140


def calculate_income_tax_owed(salary: float) -> float:
    if salary <= PERSONAL_ALLOWANCE_THRESHOLD:
        return 0

    if salary <= HIGHER_RATE_THRESHOLD:
        return _calculate_basic_rate_tax_owed(salary=salary)

    if salary <= ADDITIONAL_RATE_THRESHOLD:
        return _calculate_higher_rate_tax_owed(salary=salary)

    return _calculate_additional_rate_tax_owed(salary=salary)


def _calculate_basic_rate_tax_owed(salary: float) -> float:
    return (salary - PERSONAL_ALLOWANCE_THRESHOLD) * 0.20


def _calculate_higher_rate_tax_owed(salary: float) -> float:
    return (HIGHER_RATE_THRESHOLD - PERSONAL_ALLOWANCE_THRESHOLD) * 0.20 + (
        salary - HIGHER_RATE_THRESHOLD
    ) * 0.40


def _calculate_additional_rate_tax_owed(salary: float) -> float:
    return (
        (HIGHER_RATE_THRESHOLD - PERSONAL_ALLOWANCE_THRESHOLD) * 0.20
        + (ADDITIONAL_RATE_THRESHOLD - HIGHER_RATE_THRESHOLD) * 0.40
        + (salary - ADDITIONAL_RATE_THRESHOLD) * 0.45
    )
