from http import HTTPStatus

from starlette.testclient import TestClient

from main import app


class TestIncomeTaxesEndpoint:
    def test_calculates_correct_tax(self):
        """
        Given a salary of £33,000
        When a GET request is made to the `income-taxes/` endpoint
        Then the calculated tax owed is £4,086
        """
        # Given
        test_client = TestClient(app=app)
        salary = 33_000

        # When
        response = test_client.get("/income-taxes", params={"salary": salary})

        # Then
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"tax owed": 4_086}
