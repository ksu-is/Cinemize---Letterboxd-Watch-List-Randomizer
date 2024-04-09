#this code is from Cristiano's cristainao's Letterboxd scraper and will be modified to work with Cinemize - CSR

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Create a dictionary where the movies will be stored
movies = []

#ask for letterboxd username in order to find the watchlist page - CSR
username = input("Enter your Letterboxd username: ")

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
        image = li.find('img')
        title = image.attrs['alt']
        poster_url = image.attrs['src']

        # Add only the title each movie to the dictionary
        movies.append({'Title': title, 'Poster_URL': poster_url})

# Convert the dictionary to a CSV file
df = pd.DataFrame(movies)
df.to_csv('lb_watchlist_with_posters.csv', index=False)