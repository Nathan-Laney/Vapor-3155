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
        # Check that creating games works
        res = game_repository.game_repository_singleton.create_game(9999999,"TESTING_GAME_DATA", "Nathan", "' or 1=1;", "ADMIN", "", date.today(), 99)
        assert res is not None

        # Check that fetching game info works
        res = game_repository.game_repository_singleton.get_game_by_id(9999999)
        assert res is not None
        assert res.description == "' or 1=1;"
        assert res.developer == "ADMIN"
        assert res.game_id == 9999999
        assert res.publisher == "Nathan"
        assert res.thumbnail_link == ''
        assert res.title == "TESTING_GAME_DATA"
        assert res.rating == 99

        res = game_repository.game_repository_singleton.delete_game(9999999)
        assert res is True
