# from models import db
# from src.repositories.game_repository import game_repository_singleton
# import pytest
# from app import app

# #correct way of using it
# def test_get_all_games():
#     test_app = app.test_client()

#     created_game = game_repository_singleton.create_game(game_id = 1, title = 'Portal 2', publisher = 'Valve', description = 'Playing with Portals', developer='Valve', thumbnail_link='Vapor-3155/static/images/portal.jpeg', release_date='4/18/2011')
    # response = test_app.get('/sear')
    # assert b'<td>The Nightmare Before Christmas</td>' in response.data
    # assert b'<td>Tim Burton</td>' in response.data
    # assert b'<td>5</td>' in response.data
