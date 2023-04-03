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