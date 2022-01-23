from api.models.movie import Movie

class Actor:
    columns = ['name']
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    def build_movie(self, values):
        return Movie(values)