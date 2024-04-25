import requests
import random
import urllib.request
from urllib.error import HTTPError
from http.client import InvalidURL
from bs4 import BeautifulSoup as bs
from PIL import ImageTk, Image
from random import choice
import tkinter as tk
from requests.exceptions import ConnectionError
import threading, time
from webbrowser import open_new
from io import BytesIO


class Threader(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.daemon = True
        self.start()

    def run(self):
        button.config(state=tk.DISABLED)
        button.config(text="Running...", cursor='wait')
        cinemizer()
        button.config(state=tk.NORMAL)
        button.config(text="Run again", cursor='arrow')

#creating a function to get a user's watchlist from Letterboxd and return it in list form to be used later
def getting_user_watchlist(username):

    # Create a dictionary where the movies will be stored
    movies = []

    # Get the total number of pages
    url = f"https://letterboxd.com/{username}/watchlist/page/1/"
    response = requests.get(url)
    response = response.content
    soup = bs(response, 'html.parser')

    pp = soup.find('div', class_='paginate-pages')
    p = soup.find_all('li', class_='paginate-page')
    last_page = (p[-1].get_text())

    # Get all the movies from each page
    for i in range(1, (int(last_page) + 1)):
        url = f"https://letterboxd.com/{username}/watchlist/page/{i}/"

        response = requests.get(url)
        response = response.content
        soup = bs(response, 'html.parser')
        
        # Find the specific tags
        uls = soup.find('ul')
        lis = soup.find_all('li', class_='poster-container')
        
        # Iterate through each LI to extract the title and poster
        for li in lis:
            image = li.find('img')
            title = image.attrs['alt']
            poster_url = image.attrs['src']
            movie_url = f"https://letterboxd.com/film/{urllib.parse.quote_plus(title).replace('+', '-').lower()}/"

            # Add the title and poster URL to the list of movies
            movies.append({'Title': title, 'Poster_URL': poster_url, 'URL': movie_url})

    return movies

#creating a function to get the description of the movie, so it can be called in the cinemizer function 
def get_description(movie_url):
    response = requests.get(movie_url)
    soup = bs(response.content, 'html.parser')
    meta_tag = soup.find("meta", attrs={"name": "description"})
    return meta_tag.get("content") if meta_tag else "Description not available"

#this is where we will scrape for the poster/movie-image like we did for the description 
def get_poster(poster_url):
    response = requests.get(poster_url)
    soup = bs(response.content, 'html.parser')
    meta_tag = soup.find("meta", property="og:image")
    return meta_tag.get("content") if meta_tag else "Poster not available"

    
#This is where the randomizing occurs as well as the movie details output 
#looping it all and getting description
def cinemizer():
    while True: 
        username = input("Enter your Letterboxd username or enter 'e' to exit: ")

        if username.lower() == 'e':
            break

        movies = getting_user_watchlist(username)

        #cinemizing/randomizing the watchlist 
        cinemeized_movie = random.choice(movies)

        #get the description from the function above 
        description_content = get_description(cinemeized_movie['URL'])

        #get movie image content 
        poster_content = get_poster(cinemeized_movie['URL'])

        #putting poster on gui 
        poster_response = requests.get(poster_content)
        img = Image.open(BytesIO(poster_response.content))
        img = ImageTk.PhotoImage(img)
    
        for widget in frame2.winfo_children():
            widget.destroy()

        poster = tk.Label(master=frame2, image=img)
        poster.image = img
        poster.pack()

        link1 = tk.Label(frame2, text=cinemeized_movie['Title'], fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: open_new(cinemeized_movie['URL']))

        description_label = tk.Label(master=frame2, text=description_content)
        description_label.pack()

        frame2.pack()

# set-up the window
window = tk.Tk()
window.title("Cinemize")

# making the color of GUI resemble the color of the letterboxd app 
window.configure(bg ="#202830")

window.resizable(False, False)
frame = tk.Frame(pady = 20, padx = 20, bg ="#202830")
frame2 = tk.Frame(pady = 20, padx = 20, bg ="#202830")

# setting the size of the GUI window 
window.geometry("400x600")  

# add text
title = tk.Label(text="Watchlisting Simplified", master=frame, bg="#202830", fg="#FFFFFF")
title.pack()

description_txt =\
"Enter your Letterboxd Username:"
description = tk.Label(text=description_txt, wraplength=300, justify='left', master=frame, bg="#202830", fg="#FFFFFF")
description.pack(pady=5)

# create the entry for the profile
entry_profile1 = tk.Entry(fg="#fe8001", bg="#FFFFFF", width=33, master=frame)
entry_profile1.pack()


# create the trigger button
button = tk.Button(text="Cinemize", bg="#202830", fg="#202830", master=frame, cursor="hand2", command= lambda: Threader(name='Start-Routine'))
button.pack(pady=5)

# create error message (won't be displayed unless an error is thrown)
error = tk.Label(text="Error.", wraplength=200, justify='left', master=frame)

# pack the frame & Run it
frame.pack()
window.mainloop()
