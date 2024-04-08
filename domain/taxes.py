def calculate_income_tax_owed(salary: float) -> float:
    tax_free_allowance = 12_570
    basic_rate_threshold = 50_270

    if salary <= tax_free_allowance:
        return 0

    if salary <= basic_rate_threshold:
        return (salary - tax_free_allowance) * 0.20

    return (basic_rate_threshold - tax_free_allowance) * 0.20 + (
            salary - basic_rate_threshold
    ) * 0.40
