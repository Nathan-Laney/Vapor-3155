from flask.testing import FlaskClient

def test_all_games(test_app: FlaskClient):
    # all_games
    res = test_app.get('/all_games')
    page_data = res.data
    assert res.status_code == 200

def test_index(test_app: FlaskClient):
    # index
    res = test_app.get('/')
    page_data = res.data
    assert res.status_code == 200

def test_about(test_app: FlaskClient):
    # about
    res = test_app.get('/about')
    page_data = res.data
    assert res.status_code == 200

def test_header(test_app: FlaskClient):
    # header
    res = test_app.get('/header')
    page_data = res.data
    assert res.status_code == 200

def test_search(test_app: FlaskClient):
    # search
    res = test_app.get('/search')
    page_data = res.data
    assert res.status_code == 200

def test_profile(test_app: FlaskClient):
    # profile
    res = test_app.get('/profile')
    page_data = res.data
    assert res.status_code == 200

def test_createGame(test_app: FlaskClient):
    # createGame
    res = test_app.get('/createGame')
    page_data = res.data
    assert res.status_code == 200

def test_game_id(test_app: FlaskClient):
    # game_id
    res = test_app.get('/<game_id>')
    page_data = res.data
    assert res.status_code == 200

def test_login(test_app: FlaskClient):
    # login
    res = test_app.get('/login')
    page_data = res.data
    assert res.status_code == 200

def test_flashPage(test_app: FlaskClient):
    # flashPage
    res = test_app.get('/flashPage')
    page_data = res.data
    assert res.status_code == 200

def test_register(test_app: FlaskClient):
    # register
    res = test_app.get('/register')
    page_data = res.data
    assert res.status_code == 200

def test_resetPassword(test_app: FlaskClient):
    # resetPassword
    res = test_app.get('/resetPassword')
    page_data = res.data
    assert res.status_code == 200
