from fastapi import FastAPI

app = FastAPI()


@app.get(path="/income-taxes")
def calculate_income_taxes(salary: float) -> dict[str, int]:
    return {"tax owed": 4_086}
