from error_request import NotAcceptable
from movie import Movie


#TODO: change the name
class Matcher(object):
    def __init__(self):
        '''
            Matcher counter with object storage.
        '''
        self.counter = 0
        self.storage = []
        self.response = {'accepted': False,
                         'counter': self.counter}
 
    def create_movie(self, json_data):
        movie_data = {}
        movie_data['imdb_id'] = json_data.get('imdb_id', None)
        movie_data['title'] = json_data.get('title', None)
        movie_data['year'] = json_data.get('year', None)
        return Movie(*movie_data)

    def match(self, json_data):
        '''
            Match json according to fields.

            :type json_data: dict
        '''
        # get json required data fields
        # make sure is a dict
        if not isinstance(json_data, dict):
            raise NotAcceptable

        # if title and id are missing
        if not json_data.get('title', None) and \
                json_data.get('imdb_id', None):
            self.response['accepted'] = False
            self.response['counter'] = 0
            return self.response

        movie = self.create_movie(json_data)

        # if the storage is empty
        if not self.storage:
            self.storage.append(json_data)
        else:
            for movie_obj in self.storage:
                if movie_obj == movie:
                    self.response['accepted'] = True
                    movie.increase_counter()
                    self.response['counter'] = movie.get_counter()
                else:
                    self.storage.append(movie)
                    #TODO: here some response

        if not self.response['accepted']:
            raise NotAcceptable

        return self.response
