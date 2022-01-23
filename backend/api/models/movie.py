from api.models.actor import Actor
class Movie:
    columns = ['title', 'year']
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    def add_actor(self, name):
        self.actor = Actor([name])