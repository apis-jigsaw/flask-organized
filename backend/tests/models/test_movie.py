from api.models.movie import Movie

def test_movie_initializes_with_values():
    movie = Movie(['Shawshank', 1999])
    assert movie.title == 'Shawshank'

