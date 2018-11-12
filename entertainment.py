import fresh_tomatoes
"""importing fresh_tomatoes file in this module."""
import media
"""importing media file in this module."""


def main():
    """This is the function/method where all the objects will be initialised.

    1st object= Avengers Infinity War"""
    infinity_war = media.Movie("Avengers: Infinity War",
                               "A final showdown taking place in MCU",
                               "https://tinyurl.com/y76vs27a",
                               "https://www.youtube.com/watch?v=6ZfuNTqbHE8",
                               "27 April 2018"
                               )
    """2nd object= Deadpool"""
    deadpool = media.Movie("Deadpool",
                           "Story of one a funny mutant hero",
                           "https://tinyurl.com/ybwpuqdz",
                           "https://www.youtube.com/watch?v=gtTfd6tISfw",
                           "12 February 2016"
                           )
    """3rd object=Deadpool 2"""
    deadpool2 = media.Movie("Deadpool 2",
                            "Story of mutants fighting evil",
                            "https://tinyurl.com/yaq9ravz",
                            "https://www.youtube.com/watch?v=20bpjtCbCz0",
                            "15 May 2018"
                            )
    """4th object=Black Panther"""
    black_panther = media.Movie("Black Panther",
                                "Story of how T'Challa becoming BlackPAnther",
                                "https://tinyurl.com/ydcy64fs",
                                "https://www.youtube.com/watch?v=xjDjIWPwcPU",
                                "12 February 2018"
                                )
    """5th object= 8 mile"""
    mile_8 = media.Movie("8 Mile",
                         "Story of early days of Eminem",
                         "https://tinyurl.com/z66a7ak",
                         "https://www.youtube.com/watch?v=axGVrfwm9L4",
                         "6 November 2002"
                         )
    """6th object= Sanju"""
    sanju = media.Movie("Sanju",
                        "Story of Indian superstar Sanjay Dutt",
                        "https://tinyurl.com/ybsmwftz",
                        "https://tinyurl.com/ycwpoqzq",
                        "29 June 2018"
                        )
    """7th object=Gangs of Wasseypur"""
    gangs_of_wasseypur = media.Movie("Gangs Of Wasseypur 1",
                                     "Story of gangwar in Wasseypur",
                                     "https://tinyurl.com/ybqrhjov",
                                     "https://tinyurl.com/yazlpyc4",
                                     "22 June 2012"
                                     )
    """8th object= Gangs of Wasseypur 2"""
    gangs_of_wasseypur_2 = media.Movie("Gangs Of Wasseypur 2",
                                       "Another story of gangwar in Wasseypur",
                                       "https://tinyurl.com/ybdnv5sc",
                                       "https://tinyurl.com/y7hetm8q",
                                       "8 August 2012"
                                       )
    """9th object= Sacred Games"""
    scared_games = media.Movie("Scared Games",
                               "Thrilling story of godman",
                               "https://tinyurl.com/yam6xwyk",
                               "https://tinyurl.com/yb8sfb6c",
                               "6 July 2018"
                               )

    movies = [infinity_war, deadpool, deadpool2,
              black_panther, mile_8, sanju, gangs_of_wasseypur,
              gangs_of_wasseypur_2, scared_games]
    """here movies is the list of all the movie objects"""

    fresh_tomatoes.open_movies_page(movies)
    """This statement will parse all the object to 'open_movies_page' class."""

if __name__ == "__main__":
    main()

