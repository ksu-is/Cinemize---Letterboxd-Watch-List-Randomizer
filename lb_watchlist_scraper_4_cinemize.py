#this code is from Cristiano's cristainao's letterboxd scrpaer and will be modified to work with cinemize

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Create a dictionary where the movies will be stored
movies = {}

username = "cheshtoorder" # Replace this with your Letterboxd username

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
    
    # Iterate through each LI to extract the title and the rating
    for li in lis:
        rating = li.attrs['data-owner-rating']
        image = li.find('img')
        title = image.attrs['alt']

        # Add the title and rating of each movie to the dictionary
        movies[title] = rating

# Convert the dictionary to a CSV file
columns = ['Movie_title', 'Rating']
df = pd.DataFrame(list(movies.items()), columns = columns)
df.to_csv('lb_watchlist.csv', index = False)