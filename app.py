from flask import Flask, render_template, request, redirect, url_for
import random
from lb_watchlist_scraper_4_cinemize import getting_user_watchlist, get_description, get_poster

app = Flask(__name__)

#definting the route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
       #where a user can type in their username
       username = request.form['username']
       return redirect(url_for('cinemizer', username=username))
   else:
       #submitting the user to get the scraper to scrape 
       return render_template('index.html')

#where the movie and movie details are displayed 
@app.route('/cinemizer/<username>')
def cinemizer(username):
    #to get the watchlist 
    movies = getting_user_watchlist(username) 

    #randomly selecting the movie from watchlist
    cinemeized_movie = random.choice(movies)

    #getting the description and poster for the randomly selected movie 
    description_content = get_description(cinemeized_movie['URL'])
    poster_content = get_poster(cinemeized_movie['URL'])

    #making the details appear 
    return render_template('movie_details.html', username=username, movie=cinemeized_movie, description=description_content, poster=poster_content)

if __name__ == '__main__':
    app.run(debug=False)