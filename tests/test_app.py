import pytest
from app import app
import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_empty_quotes_list_does_not_crash_app(client, mocker):
    """
    Tests that the application does not crash if the QUOTES list is empty
    and instead displays a default quote.
    """
    mocker.patch('app.QUOTES', [])
    response = client.get('/')
    assert response.status_code == 200
    assert b"Be the change you wish to see in the universe." in response.data
