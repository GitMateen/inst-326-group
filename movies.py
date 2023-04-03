"""
    This is a simple file to practice using github.
"""

def example_dict(our_dict):
    """
        To create a dictionary of movies.

    Args:
        our_dict(dct): A dictionary of movies, rating, description, and year.
    
    returns:
        our_dict(dct): All the movies.
    """
    our_dict["2023"] = {"movie": "Creed 3", "rating": 5, "description": "The third creed movie, great boxing series and I would highly recommend watching."}
    our_dict["2012"] = {"movie": "The Avengers", "rating": 5, "description": "The first avengers movie, great action."}
    return our_dict

def easy_movies(ez_dict):
    """A dictionary of the most popular/likely to be known movies.
    
    Args:
        ez_dict (dict): A dictionary of 'easy' movies with their rating, description, and year.
        
    Returns:
        ez_dict (dict): All the easy movies
    """
    ez_dict["2006"] = {"movie": "Cars", "rating": 4.7, "description": "Computer-animated sports comedy film by Pixar Animation Studios. The first Cars series movie."}
    ez_dict["1997"] = {"movie": "Titanic", "rating": 4.8, "description": "Action-packed romance set against the ill-fated maiden voyage of the Titanic."}
    return ez_dict