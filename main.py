from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_webiste = response.text

soup = BeautifulSoup(movie_webiste, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")
all_movies = []
for title in movie_titles:
    movie_title = title.getText()
    all_movies.append(movie_title)

movies_in_order = all_movies[::-1]

with open("movies.txt", "a") as file:
    file.write("Top 100 Movies Of All Time\n")
    for movie in movies_in_order:
        file.writelines(f"\n{movie}")
