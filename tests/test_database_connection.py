from flask.testing import FlaskClient
from models import db
from app import app
import api_calls
from src.repositories import game_repository, tag_repository, tag_game_repository
from datetime import date

def test_api_connection(test_app: FlaskClient):
    with app.app_context():
        # Check game_api is working 
        res = api_calls.search_db("Fortnite")
        assert res is not None


def test_db_connection(test_app: FlaskClient):
    with app.app_context():
        # Check game_api is working 
        res = game_repository.game_repository_singleton.create_game(9999999,"TESTING_GAME_DATA", "Nathan", "' or 1=1;", "ADMIN", "", date.today(), 99)
        assert res is not None

