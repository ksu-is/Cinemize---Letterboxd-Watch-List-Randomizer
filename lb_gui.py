'''
This is code is to run the actual software. Makesure to look at the README file and follow the directions. 
'''

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
import webbrowser

# Define the Threader class
class Threader(threading.Thread):
    def __init__(self, button, username, *args, **kwargs):
        self.button = button
        self.username = username
        threading.Thread.__init__(self, *args, **kwargs)
        self.daemon = True
        self.start()

    def run(self):
        self.button.config(state=tk.DISABLED)
        self.button.config(text="Cinemizing...", cursor='wait')
        cinemizer(self.username)
        self.button.config(state=tk.NORMAL)
        self.button.config(text="Cinemize", cursor='arrow')

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
def cinemizer(username):
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

    #displays title in the Cinemize GUI 
    link1 = tk.Label(frame2, text=cinemeized_movie['Title'], fg="white", bg="#202830", cursor="hand2", font=("Arial", 24, "underline"))
    link1.pack()
    link1.bind("<Button-1>", lambda e: open_new(cinemeized_movie['URL']))

    #displays the description of the movie 
    description_label = tk.Label(master=frame2, text=description_content, fg="white", bg="#202830", wraplength=500)
    description_label.pack()

    #displays the movie image/poster
    poster = tk.Label(master=frame2, image=img)
    poster.image = img
    poster.pack()

    frame2.pack()

#function to hyperlink letterboxd to 
def open_letterboxd(event):
    webbrowser.open_new("https://letterboxd.com/")

# set-up the window
window = tk.Tk()
window.title("Cinemize")

# making the color of GUI resemble the color of the letterboxd app 
window.configure(bg ="#202830")

window.resizable(False, False)
frame = tk.Frame(pady = 20, padx = 20, bg ="#202830")
frame2 = tk.Frame(pady = 20, padx = 20, bg ="#202830")

# setting the size of the GUI window 
window.geometry("800x800")  

# adding header text
title = tk.Label(text="Watchlisting Simplified", master=frame, bg="#202830", fg="#fe8001", font=("Helvetica", 16, "bold"))
title.pack()

#adding the prompt 
description_txt = "Enter your "
description_txt += "Letterboxd"  # Make "Letterboxd" a hyperlink
description_txt += " username:"

#hyperlinking the prompt to letterboxd 
# Create a label for the prompt
description = tk.Label(master=frame, text=description_txt, bg="#202830", fg="#03df54", font=("Helvetica", 16))
description.pack()

# Bind the hyperlink behavior to the label
description.bind("<Button-1>", open_letterboxd)

# creating the entry for the profile
username_entry = tk.Entry(fg="#41bbf2", bg="#202830", width=33, master=frame, justify="center", font=("Helvetica", 13, "bold"))
username_entry.pack()


# creating the trigger button
button = tk.Button(
    text="Cinemize",
    bg="#202830",
    fg="#202830",
    master=frame,
    cursor="hand2",
    command=lambda: Threader(button, username_entry.get())
)
button.pack(pady=5)

# creating error message (won't be displayed unless an error is thrown)
error = tk.Label(text="Error.", wraplength=200, justify='left', master=frame)

# pack the frame & Run it
frame.pack()
window.mainloop()

