# from models import db
# from src.repositories.game_repository import game_repository_singleton
# import pytest
# from app import app

# from tests.unit.utils import create_game
# from src.models import game, db
# from flask.testing import FlaskClient
# from tests.unit.utils import create_game


# def test_get_all_games(test_app: FlaskClient):
#     #test_app = app.test_client()

#     test_game = create_game()

#     created_game = game_repository_singleton.create_game(game_id = 1, title = 'Portal 2', publisher = 'Valve', description = 'Playing with Portals', developer='Valve', thumbnail_link='Vapor-3155/static/images/portal.jpeg', release_date='4/18/2011')
#     # response = test_app.get('/sear')
#     # assert b'<td>The Nightmare Before Christmas</td>' in response.data
#     # assert b'<td>Tim Burton</td>' in response.data
#     # assert b'<td>5</td>' in response.data
#     db.session.add(created_game)

# def test_get_all_movies(test_app: FlaskClient):

#         refresh_db()
#         test_movie = create_movie()

#         res = test_app.get('/movies')
#         page_date: str = res.data.decode()

#         assert res.status_code == 200
#         assert f'<td><a href="/movies/{test_movie.movie_id}">The Dark Knight</a></td>' in page_date
#         assert '<td>Christpther Nolan</td>' in page_date
#         assert '<td>5</td>' in page_date


# def test_get_all_movies_empty(test_app: FlaskClient):

#     refresh_db()

#     res = test_app.get('/movies')
#     page_date: str = res.data.decode()

#     assert res.status_code == 200
#     assert '<td>' not in page_date

# def test_get_single_movie(test_app: FlaskClient):
#     refresh_db()
#     test_movie = create_movie()

#     res = test_app.get(f'/movies/{test_movie.movie_id}')
#     page_date: str = res.data.decode()
# assert res.status_code == 200
#     assert '<h1>The Dark Knight - 5</h1>' in page_date
#     assert '<h2>Christpther Nolan</h2>' in page_date

# def test_get_single_movie_404(test_app: FlaskClient):
#     refresh_db() 
#     res = test_app.get('/movies/1')
#     assert res.status_code == 404


# def test_create_movie(test_app: FlaskClient):
#     refresh_db()

#     res = test_app.post('/movies', data={
#         'title': 'The Dark Knight',
#         'director': 'Christpther Nolan',
#         'rating': 5
#     }, follow_redirects=True)
#     page_date: str = res.data.decode()

#     assert res.status_code == 200
#     assert '<h1>The Dark Knight - 5</h1>' in page_date
#     assert '<h2>Christpther Nolan</h2>' in page_date

#     test_movie = Movie.query.filter_by(title='The Dark Knight').first()
#     assert test_movie is not None
#     assert test_movie.title == 'The Dark Knight'
#     assert test_movie.rating == 5




# def test_create_movie_404(test_app: FlaskClient):
#     refresh_db()
#     res = test_app.post('/movies', data={}, follow_redirects=True)
#     assert res.status_code == 400