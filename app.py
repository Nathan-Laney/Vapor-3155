#      :::     :::           :::        :::::::::       ::::::::       ::::::::: 
#     :+:     :+:         :+: :+:      :+:    :+:     :+:    :+:      :+:    :+: 
#    +:+     +:+        +:+   +:+     +:+    +:+     +:+    +:+      +:+    +:+  
#   +#+     +:+       +#++:++#++:    +#++:++#+      +#+    +:+      +#++:++#:    
#   +#+   +#+        +#+     +#+    +#+            +#+    +#+      +#+    +#+    
#   #+#+#+#         #+#     #+#    #+#            #+#    #+#      #+#    #+#     
#    ###           ###     ###    ###             ########       ###    ###      

# Nathan Laney, Kaitlyn Finberg, Sumi Verma, Tyler Minnis, Honna Sammos
# Created for UNC Charlotte
# ITSC 3155 - Software Engineering with Jacob Krevat 

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt
import os
from models import db
from datetime import date, datetime
import api_calls                              # UNCOMMENT FOR FRONTEND
from werkzeug.utils import secure_filename

# Imports for our database tables. These are in a specific order, 
# to correctly populate the foreign keys. 
# Having these imports allows for them to be created on flask run
# if they do not already exist

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
    print("____________________WITH CONTEXT_____________________")
    # api_calls.populate_tags()
    # api_calls.populate_games(500)
    # all_tags = tag_repository_singleton.get_all_tags()
    # print(all_tags)
    # for i in all_tags:
    #     print(i.tag_description)
    
    # all_users = user_repository_singleton.get_all_users()
    # print(all_users)
    # doom = game_repository_singleton.create_game_without_an_id("DOOM", "idSoftware", "the classic shooter but in 2016 graphics", "idSoftware", "www.google.com", date.today())
    # asdhhdsa = game_repository_singleton.get_all_games()
    # print(asdhhdsa)
    # print(game_repository_singleton.get_game_by_id(144104).title)
    # api_calls.search_db("Fortnite")
    # api_calls.fast_search_db("Project")

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
    api_calls.search_db(q)
    search_result_array = game_repository_singleton.search_games_by_title(title = q)
    search_result_array_length = len(search_result_array)
    return render_template('search.html', results_found = search_result_array_length, search_results=search_result_array, search_query=q)

@app.get('/all_games')
def all_games():
    return render_template('all_games.html')

#kaitlyn is doing things and crying while dylan watches and judges 
@app.get('/profile')
def profile():
    current_page = "profile"
    #TODO: get the current session user STATUS: Done
    # current_user = User.query.filter_by(user_id=session['user']['user_id']).first() OLD
    current_user = user_repository_singleton.get_user_by_id(user_id=session['user']['user_id'])
    #print(current_user.username)
    #TODO: If the user isnt logged in, dont let them go to the profile page STATUS: Almost Complete
    #getting a Key Error
    return render_template('profile.html', current_user=current_user, profile_path=session['user']['profile_path'])



@app.get('/post_review')
def post_review():    
    return render_template('post_review.html')


@app.get('/gamepage')

def gamepage():
    current_page = "gamepage"
    #single_game = game_repository.get_game_by_id(game_id)
    #existing_game = Game.query.filter_by(single_game=single_game).first()
    return render_template('gamepage.html') #existing_game=existing_game


# This is the start of the login in logic


@app.get('/login')
def login():
    return render_template('login.html')


@app.post('/login')
def loginform():
    password = request.form.get('password')
    email = request.form.get('email')
    if (email == None):
        return redirect('login')
    if (password == None):
        return redirect('login')

    print(email)
    print(password)

    existing_user = user_repository_singleton.get_user_by_email(email=email) #type: ignore

    if not existing_user:
        return redirect('/login')

    #if not bcrypt.check_password_hash(existing_user.password, password):
        #return redirect('/login')

    session['user'] = {
        'user_id': existing_user.user_id,
        'profile_path': existing_user.profile_path
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


#found some errors in register. login should work fine when these are fixed
@app.post('/register')
def registerForm():
    #username resturning null
    user_id = request.form.get('user_id')
    username = request.form.get('user_name')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    email = request.form.get('email')
    # existing_user = user_data.query.filter_by(username=username).first()
    # existing_email = user_data.query.filter_by(email=email).first()

#     if (existing_email and existing_user):
#         return redirect('/login')


    bcryptRounds = int(os.getenv('BCRYPT_ROUNDS', 4)) # second parameter is the default fallback

    print(password)
    print(bcryptRounds)
    #rounds caused this to fail
    hashed_bytes = bcrypt.generate_password_hash(
        password, bcryptRounds)
    hashed_password = hashed_bytes.decode('utf-8')

    #Kaitlyn- Save the profile picture 
    if 'profile' not in request.files:
        return redirect('/')

    profile_picture = request.files['profile']
    if (profile_picture.filename == None) :
        return redirect('/')

    if profile_picture.filename == '':
        return redirect('/')
    
    if profile_picture.filename.rsplit('.', 1)[1].lower() not in ['jpg', 'jpeg', 'png', 'gif']:
        return redirect('/')

    safe_filename = secure_filename(f'{user_id}-{profile_picture.filename}')

    profile_picture.save(os.path.join('static', 'profile-pics', safe_filename))

    #added username=username, password=hashed_password, etc bc it wouldnt work without it
    if (email == None):
        return redirect('login')
    if (first_name == None):
        return redirect('login')
    if (username == None):
        return redirect('login')
    new_user = user_repository_singleton.create_user(username=username, password=hashed_password, first_name=first_name, email=email, profile_path=safe_filename)
    
    db.session.add(new_user)
    db.session.commit()
    return redirect('/login')

@app.get('/resetPassword')
def resetPassword():
    return render_template('resetPassword.html')


@app.post('/logout')
def logout():
    session.pop('user')
    return redirect('/')


if __name__ == '__main__':
    app.run()

#@app.get('/secret')
