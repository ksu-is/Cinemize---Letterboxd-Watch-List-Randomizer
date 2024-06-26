# Cinemize - a watchlist randomizer

Cinemize, a combination of the words cinema and randomize. The target users of the software are adamant movie watchers, specifically Letterboxd users. Sometimes it can be tedious to choose from so many great options, which is where Cinemize comes in to simplfy the movie picking processing by combing through Letterboxd users massive Watchlist catalogs. 

### Letterboxd 

Letterboxd is a cinephile’s favorite social media. The application has evolved to allow users to keep a running list of films they want to watch called a Watchlist. In addition to the Watchlsit feature, Letterboxd users can keep track of films they have watched, rate and review films, display their four favorite films, and interact with other cinephiles. Check it out for yourself: https://letterboxd.com/ 

## Usage

Cinemize scrapes a user’s Letterboxd web page immediately after the user enters their username as prompted. Cinemize then finds the user’s public Watchlist and creates a list of strings from the titles of the movie Watchlist. After reformatting the new list, the software outputs a random item from the user's Watchlist alongside its poster and a description of the movie. For the user to get multiple recommendations, the user must keep their username in the search bar and continue pressing the Cinemize button. Additionally, there is a link on the web page that can take the user directly to Letterboxd.

### Instructions

#### note: the longer your watchlist the longer the program will take to run.

1) Run installations in terminal
    -m pip install requests <br>
    -m pip install bs4 <br>
    -m pip install pandas <br>
    -m pip install random <br>
    -m pip install urllib.parse <br>
    -m pip install urllib.request <br>
    -m pip install webbrowser <br>
    -m pip install urllib.error <br>
    -m pip install  http.client <br>
    -m pip install bs4 <br>
    -m pip install PIL <br>
    -m pip install tkinter <br>
    -m pip install requests.exceptions <br>
    -m pip install threading <br>
    -m pip install webbrowser <br>
    -m pip install io 

2) Run lb_gui.py and wait for the Cinemize window to appear

3) Enter your letterboxd username in the box below "enter your Letterboxd username:" (be aware of case sensitivity)

4) Press the Cinemize button

5) Optional: Leave your Letterboxd username in the text box and press Cinemize to get another movie. 

#### Tips: 
    - If Cinemize is stuck on the spinning wheel of death, exit the browser and re-run the GUI. 
    - You can click on "Letterboxd" in the "Enter your Letterboxd username:" to open Letterboxd

## Credits

A special thanks to Cristiano (https://github.com/cristianooo1/Letterboxd-watchlist-scraper) for creating a Letterboxd Watchlist scraper that was modified to make Cinimize. 

Thank you to GeeksforGeeks (https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/)!! In order to make this program work I referenced their guide to implement beautiful soup.

Lastly, a special thanks to Samir (https://github.com/samirsaliba/letterboxd-watchlist-picker) for creating a python GUI that was modiified to host Cinemize's interface.