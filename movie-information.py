import imdb

# creamos la instanacia
ia = imdb.Cinemagoer()
movie = input('Enter the movie name: ')

items = ia.search_movie(movie)
# print(items)

for index, movies in enumerate(items):
    title = movies.get('title', 'no data')
    year = movies.get('year', 'no data')
    print(f"{index + 1}. {title} ({year})")