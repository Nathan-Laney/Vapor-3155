import pytest
from app import app

@pytest.fixture(scope='module')
def test_app():
    return app.test_client()