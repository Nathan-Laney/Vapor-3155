# Nathan Laney, Kaitlyn Finberg, Sumi Verma, Tyler Minnis, Honna Sammos
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt
import os
from models import db
from datetime import date, datetime

# Imports for our database tables. These are in a specific order, 
# to correctly populate the foreign keys. 
# Having these imports allows for them to be created on flask run
# if they do not already exist
from src.models.user_data import user_data

from src.repositories.tag_repository import tag_repository_singleton
from src.repositories.game_repository import game_repository_singleton
from src.repositories.user_repository import user_repository_singleton

load_dotenv()
app = Flask(__name__)

print(os.getenv('SQLALCHEMY_DATABASE_URI'))
# postgresql://username:password@host:port/database_name
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.secret_key = os.getenv('APP_SECRET_KEY')

db.init_app(app)
bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()
    
    print("____________________DEBUG_____________________")
    all_tags = tag_repository_singleton.get_all_tags()
    print(all_tags)
    # for i in all_tags:
    #     print(i.tag_description)
    
    all_users = user_repository_singleton.get_all_users()
    print(all_users)
    doom = game_repository_singleton.create_game_without_an_id("DOOM", "idSoftware", "the classic shooter but in 2016 graphics", "idSoftware", "www.google.com", date.today())
    asdhhdsa = game_repository_singleton.get_all_games()
    print(asdhhdsa)
    print("____________________________________________________")

@app.get('/')
def index():
    return render_template('index.html')


@app.route('/header')
def header():
    return render_template('index.html')


@app.get('/about')
def about():
    return render_template('about.html')


@app.get('/search')
def search():
    q = request.args.get('q', '')
    return render_template('search.html', search_query=q)


@app.get('/all_games')
def all_games():
    return render_template('all_games.html')


@app.get('/profile')
def profile():
    return render_template('profile.html')


@app.get('/post_review')
def post_review():    
    return render_template('post_review.html')


@app.get('/gamepage')
def gamepage():    
    return render_template('gamepage.html')

# This is the start of the login in logic


@app.get('/login')
def login():
    return render_template('login.html')


@app.post('/login')
def loginform():
    password = request.form.get('password')
    email = request.form.get('email')

    existing_user = user_data.query.filter_by(email=email).first()

    if not existing_user:
        return redirect('/login')

    if not bcrypt.check_password_hash(existing_user.password, password):
        return redirect('/login')

    session['user'] = {
        'user_id': existing_user.user_id
    }
    return redirect('/youGotIn')
# this is a post... you might have to make a get so that the page will load.....


@app.get('/youGotIn')
def temp():
    return render_template('youGotIn.html')


@app.get('/register')
def register():
    current_page = "register"
    return render_template('register.html')


# @app.post('/register')
# def registerForm():
#     username = request.form.get('user_name')
#     password = request.form.get('password')
#     first_name = request.form.get('first_name')
#     email = request.form.get('email')
#     existing_user = user_data.query.filter_by(username=username).first()
#     existing_email = user_data.query.filter_by(email=email).first()

#     if (existing_email and existing_user):
#         return redirect('/login')

#     bcryptRounds = os.getenv('BCRYPT_ROUNDS')
#     if bcryptRounds == 'None':
#         print("Defaulting bcryptRounds (error)")
#         bcryptRounds = 20000 # If bcrypt rounds is not found, falls back to default value of 20k

#     hashed_bytes = bcrypt.generate_password_hash(
#         password, bcryptRounds)
#     hashed_password = hashed_bytes.decode('utf-8')

#     new_user = user_data(username, hashed_password, first_name, email)
#     db.session.add(new_user)
#     db.session.commit()
#     return redirect('/login')


@app.get('/resetPassword')
def resetPassword():
    return render_template('resetPassword.html')


@app.post('/logout')
def logout():
    session.pop('user')
    return redirect('/')


if __name__ == '__main__':
    app.run()
