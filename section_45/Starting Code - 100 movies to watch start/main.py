import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
data = response.content

soup = BeautifulSoup(data, "html.parser")


movies_titles = soup.find_all(name="h3", class_="title")

top_100_movies = [movie.getText().split(" ", 1)[1] for movie in movies_titles]
top_100_movies.reverse()
with open("movies.txt", "a+") as my_file:
    for index, movie in enumerate(top_100_movies):
        my_file.write(f"{index+1}) {movie}\n")
