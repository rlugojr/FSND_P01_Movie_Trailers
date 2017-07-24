
'''The media.Movie Class provides a data structure to store
 movie related information'''


class Movie():

    '''The media.Movie constructor is used to instantiate a movie object.
        Inputs (required):
            movie_title --> Title of the movie.
            movie_year --> The year the movie was released.
            movie_storyline --> Tagline or Storyline of the movie.
            poster_image --> The url to the image file for the movie poster.
            trailer_youtube --> The url to the YouTube video for
                                the movie trailer.
        Outputs: Movie Object'''
    def __init__(self, movie_title, movie_year, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
