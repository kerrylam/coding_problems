"""Users on longer flights like to start a second movie right when their first 
one ends, but they complain that the plane usually lands before they can see the 
ending. So you're building a feature for choosing two movies whose total 
runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of 
integers movie_lengths (in minutes) and returns a boolean indicating whether 
there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory
"""

def two_inflight_movies(flight_length=int, movie_lengths=list):
    """return whether flight allows for two movies to finish."""
    seen_movies = set()

    for first_watched_movie in movie_lengths:
        matched_movie = flight_length - first_watched_movie
        if matched_movie in seen_movies:
            return True
        else:
            seen_movies.add(first_watched_movie)
    return False


print(two_inflight_movies(120, [40, 60, 100, 80]))
print(two_inflight_movies(120, [140, 60, 100, 80]))
print(two_inflight_movies(120, [40, 160, 100, 80]))