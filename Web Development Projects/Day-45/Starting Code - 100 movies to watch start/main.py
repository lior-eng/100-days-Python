import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
archive_web_page = response.text

soup = BeautifulSoup(archive_web_page, "html.parser")


all_movies = soup.find_all(name= "h3", class_= "title")

movies_reversed = [movie.getText() for movie in all_movies]
movies = movies_reversed[::-1]

print(movies)

with open("./Web Development Projects/Day-45/"
        "Starting Code - 100 movies to watch start/Top-100.txt",
          mode= "w",
          encoding= "utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")