import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/list/ls055592025/"

response = requests.get(URL)
wesite_html = response.text


soup = BeautifulSoup(wesite_html, "html.parser")

all_movies = soup.select(selector="h3 a")
print(all_movies)

movie_index = 1
file = open("movies.txt", "w")

for movie in all_movies:
    movie_name = movie.string
    print(file.write(f"\n {(movie_index)}. {movie_name}"))
    movie_index +=1

file.close()