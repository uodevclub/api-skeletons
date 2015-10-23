from imdb import IMDb
ia = IMDb()

# Search for a movie
movie_search = ia.search_movie('The Martian')
movie = movie_search[0]

# Fetch more info about a movie
ia.update(movie)

# Movie title 
movie['title']

# Movie plot
movie['plot']

# Movie cast
movie['cast']


# Person object
person = movie['cast'][0]

# Fetch more info about a person
ia.update(person)

# Person name
person['name']

# Person headshot
person['headshot']


# Search for a person
person_search = ia.search_person('Matt Damon')