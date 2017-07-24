import media

"""
    Contains the data used to instantiate new media.Movie objects.
    A media.Movie is instantiated as follows:
    movie_object = media.Movie(title,
                               year,
                               storyline,
                               poster_image_url,
                               trailer_youtube_url
    )
"""
toy_story = media.Movie("Toy Story",
                        "1995",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "2009",
                     "A Marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

die_hard = media.Movie("Die hard",
                       "1988",
                       "40 Stories Of Sheer Adventure!",
                       "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg",
                       "https://www.youtube.com/watch?v=QIOX44m8ktc")

logan = media.Movie("Logan",
                    "2017",
                    "His time has come.",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

true_romance = media.Movie("True Romance",
                           "1993",
                           "Stealing, Cheating, Killing. Who said romance is dead?",
                           "https://upload.wikimedia.org/wikipedia/en/d/d6/True_romance.jpg",
                           "https://www.youtube.com/watch?v=_wNYNDzKpuQ")

pulp_fiction = media.Movie("Pulp Fiction",
                           "1994",
                           "You won't know the facts until you've seen the fiction.",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

#assign the movie objects to the movie list that will be used to generate the web site.
movie_list = [toy_story, avatar, die_hard, logan, true_romance, pulp_fiction]
