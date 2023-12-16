"""Get some movies from the MovieCatalog and print them.

In the movies.csv in the starter code, line 4 has a deliterate
error in the data for Mulan.

Things to look for are:
- MovieCatalog does not fail or stop reading movie data on first error
- with the uncorrected data, get_movie("Mulan") returns the 2020 version
- with the corrected data, get_movie("Mulan") returns the 1998 version

"""

# Student wrote MovieCatalog in different files.
# These are the most common ones, but you may need to add an import.
try:
    from moviecatalog import MovieCatalog
except Exception:
    pass
try:
    from movie_catalog import MovieCatalog
except Exception:
    pass
try:
    from catalog import MovieCatalog
except Exception:
    pass

from movie import *

def prompt(message):
    print("")
    input(message)

# No score for this but for my info.
print("Is MovieCatalog a Singleton?")
catalog1 = MovieCatalog()
catalog2 = MovieCatalog()
print(catalog1 is catalog2)

# In the starter movies.csv there is a deliberate error
# in the data for this movie.
# Therefore, if you use the original 'movies.csv' file,
# it should print the 2020 'Mulan' but after correction 
# show the 1998 version.
prompt("Get Mulan.  Should return 1998 version only on corrected movies.csv.")
movie = catalog1.get_movie("Mulan")
print("Result:", movie)
print(movie.year)

prompt("Get Mulan,2020.  Should return 2020 version.")
movie = catalog1.get_movie("Mulan", 2020)
print("Result:", movie)
print(movie.year)

prompt("Get Oppenheimer")
movie = catalog1.get_movie("Oppenheimer")
print("Result:", movie)

prompt("Get Mulan,2022.  Should return None")
movie = catalog1.get_movie("Mulan", 2022)
print("Result:", movie)
