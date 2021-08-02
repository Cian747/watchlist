from flask import render_template
from app import app
from .request import get_movies

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The best Movie Review Website Online'
    message = 'Welcome to Tazama'
    return render_template('index.html',message = message,title = title,popular = popular_movies, upcoming = upcoming_movie,now_showing= now_showing_movie)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie_id = 'If not today then tomorrow.'
    return render_template('movie.html',movie_id = movie_id)