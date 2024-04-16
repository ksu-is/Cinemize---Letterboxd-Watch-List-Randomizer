#this code is from Cristiano's cristainao's Letterboxd scraper and will be modified to work with Cinemize - CSR

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import random
import urllib.parse

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

#this is where we will scrape for the poster like we did for the description 
def get_poster(poster_url):
    response = requests.get(poster_url)
    soup = bs(response.content, 'html.parser')
    meta_tag = soup.find("meta", property="og:image")
    return meta_tag.get("content") if meta_tag else "Poster not available"

    
#looping it all and getting description
def cinemizer():
    while True: 
        username = input("Enter your Letterboxd username or enter 'e' to exit: ")

        if username.lower() == 'e':
            break

        movies = getting_user_watchlist(username)

        #cinemizing the watchlist 
        cinemeized_movie = random.choice(movies)

        #get the description from the function above 
        description_content = get_description(cinemeized_movie['URL'])

        #get poster content 
        poster_content = get_poster(cinemeized_movie['URL'])

    
#getting descirption of movie 
        #for movie in movies:
            #encoding title based off of recommendation by chatgpt 
            #encoded_title = urllib.parse.quote_plus(movie['Title']).replace("+", "-").lower()

            #url = f"https://letterboxd.com/film/{encoded_title}/"
            #response = requests.get(url)
            #soup = bs(response.content, 'html.parser')
            #meta_tag = soup.find("meta", attrs={"name": "description"})
            #description_content = meta_tag.get("content") if meta_tag else "Description not available"

        #the output
        print('\n')
        print("Cinemized Movie from "+ username + "'s " + 'Watchlist:')
        print("Title:", cinemeized_movie['Title'])
        print("Description:", description_content)
        print("Poster:", poster_content)
        print('\n')

cinemizer()