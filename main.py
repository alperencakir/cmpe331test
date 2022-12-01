"""
    Stage: Development-01
    @author: Gökalp Çevik, 120202074
    @author: Alperen Çakır, 117200088
"""

import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/top/'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

mov_name_rating_dict = dict()
mov_names = []
mov_ratings = []

mov_i = 0
rating_i = 0

for movie_name in soup.find_all('td',attrs={'class':'titleColumn'}):
    mov_names.append(movie_name.get_text()) 

for imdb_rating in soup.find_all('td',attrs={'class':'ratingColumn imdbRating'}):
    mov_ratings.append(imdb_rating.get_text())


for i in range(0,len(mov_names)):
    print("Movie Name:",mov_names[i], "IMDB Rating:",mov_ratings[i],sep="")
    print('-----------------')

