# FSND P01 Movie Trailers Web Site

The purpose of this project is to apply an object oriented approach to the back-end design of a movie web site.

The data in "movie_data.py" is used to instantiate "movie" objects using a custom class, defined in "media.py",
named "media.Movie()" which is structured as follows:

    media.Movie(title,
                year,
                storyline,
                poster_image_url,
                trailer_youtube_url)

The instantiated "movie" objects are stored in a list named "movie_list", which is used by "fresh_tomatoes.py"
to render the HTML for the web page.

"entertainement_center.py" is responsible for pulling the movie data, which generates the instances of class "media.Movie"
and then executes "fresh_tomatoes.py", which generates the web site HTML file and launches it in a browser.

* * *

## How to use Movie Trailers Web Site.

To use this project you must have Python 2.7 installed.

1.  Download the code or clone the repository.
2.  Open a command line or terminal session.
3.  Change working directory to the folder with the downloaded source code.
4.  Execute "python entertainment.py".
5.  Enjoy the trailers of a few of my favorite movies!
