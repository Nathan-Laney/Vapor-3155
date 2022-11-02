# Nathan Laney, Kaitlyn Finberg, Sumi Verma, Tyler Minnis, Honna Sammos
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__) 

@app.get('/')
def home():
    return render_template('index.html') 

@app.get('/about.html')
def about():
    return render_template('about.html') 

@app.get('/search.html')
def search():
    return render_template('search.html') 

@app.get('/all_games.html')
def all_games():
    return render_template('all_games.html') 

@app.get('/profile.html')
def profile():
    return render_template('profile.html') 

@app.get('/post_review.html')
def post_review():
    return render_template('post_review.html') 

@app.get('/gamepage.html')
def gamepage():
    return render_template('gamepage.html') 
