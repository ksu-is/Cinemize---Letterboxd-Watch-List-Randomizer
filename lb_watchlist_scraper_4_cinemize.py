#this code is from Cristiano's cristainao's Letterboxd scraper and will be modified to work with Cinemize - CSR

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import random

#creating a function out of this entire process to pick a random movie from a uesr's watchlist 
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
            
            # Add the title and poster URL to the list of movies
            movies.append({'Title': title, 'Poster_URL': poster_url})

    return movies

#ask for letterboxd username in order to find the watchlist page - CSR
username = input("Enter your Letterboxd username: ")

#get the user's watch list
movies = getting_user_watchlist(username)

#cinemizing (randomly choosing a movie) the watch list 
cinemized_movie = random.choice(movies)

#printing the stuff from randomized movie function
print("Cinemized Movie from "+ username + "'s " + 'Watchlist:')
print("Title:", cinemized_movie['Title'])
print("Poster (URL for now):", cinemized_movie['Poster_URL'])


