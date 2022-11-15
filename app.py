# Nathan Laney, Kaitlyn Finberg, Sumi Verma, Tyler Minnis, Honna Sammos
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__) 

page_index = {
    1   :   "index",
    2   :   "about",
    3   :   "all_games",
    4   :   "search",
    5   :   "other"
}

current_page = "index"

@app.get('/')
def index():
    current_page = "index"
    return render_template('index.html') 

@app.route('/header')
def header():
    current_page = "index"
    return render_template('index.html')
    
@app.get('/about')
def about():
    current_page = "about"
    return render_template('about.html') 

@app.get('/search')
def search():
    q = request.args.get('q', '')
    current_page = "search"
    return render_template('search.html', search_query=q) 

@app.get('/all_games')
def all_games():
    current_page = "all_games"
    return render_template('all_games.html') 

@app.get('/profile')
def profile():
    current_page = "profile"
    return render_template('profile.html') 

@app.get('/post_review')
def post_review():
    current_page = "post_review"
    return render_template('post_review.html') 

@app.get('/gamepage')
def gamepage():
    current_page = "gamepage"
    return render_template('gamepage.html') 

if __name__ == '__main__':
    app.run()