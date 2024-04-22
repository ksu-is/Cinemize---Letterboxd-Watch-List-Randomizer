# Cinemize - a watchlist randomizer

Cinemize, a combination of the words cinema and randomize. The target users of the software are adamant movie watchers, specifically Letterboxd users. Sometimes it can be tedious to choose from so many great options, which is where Cinemize comes in to simplfy the movie picking processing by combing through Letterboxd users massive Watchlist catalogs. 

### Letterboxd 

Letterboxd is a cinephile’s favorite social media. The application has evolved to allow users to keep a running list of films they want to watch called a Watchlist. In addition to the Watchlsit feature, Letterboxd users can keep track of films they have watched, rate and review films, display their four favorite films, and interact with other cinephiles. Check it out for yourself: https://letterboxd.com/ 

## Usage

Cinemize scrapes a user’s Letterboxd web page immediately after the user enters their username as prompted. Cinemize then finds the user’s public Watchlist and creates a list of strings from the titles of the movie Watchlist. After reformatting the new list, the software outputs a random item from the user's Watchlist alongside its poster and a description of the movie. For the user to get multiple recommendations, the user must keep their username in the search bar and continue pressing the Cinemize button. Additionally, there is a link on the web page that can take the user directly to Letterboxd.

### Instructions

#### note: the longer your watchlist the longer the program will take to run.

1) Run installations in a terminal, if necessary 
    -m pip install requests
    -m pip install bs4
    -m pip install pandas
    -m pip install random
    -m pip install urllib.parse

2) (update when I can figure out the flask and etc)


## Credits

A special thanks to Cristiano (https://github.com/cristianooo1/Letterboxd-watchlist-scraper) for creating a Letterboxd Watchlist scraper that was modified to make Cinimize. 

In order to make this program work I also referenced a guide to implement beautiful soup. Thank you to GeeksforGeeks! (https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/)
