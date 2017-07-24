import movie_data
import fresh_tomatoes

#retrieve movie list from movie_data.py.
#this also creates instances of movie objects
#and populates.
movies = movie_data.movie_list

#generate the web page using the movie_list
#and displays it in the browser.
fresh_tomatoes.open_movies_page(movies)
