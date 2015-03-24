from error_request import NotAcceptable
from movie import Movie


#TODO: change the name
class Matcher(object):
    def __init__(self):
        '''Matcher counter with object storage.
        '''
        self.storage = []
        self.response = {'accepted': False,
                         'counter': 0}

    def create_movie(self, json_data):
        '''Creates Movie() object.

        :type json_data: dict
        :param json_data: movie data in json format

        :rtype Movie: Movie object
        :returns: created movie object
        '''
        movie_data = {}
        movie_data['imdb_id'] = json_data.get('imdb_id', None)
        movie_data['title'] = json_data.get('title', None)
        movie_data['year'] = json_data.get('year', None)
        movie_data['description'] = json_data.get('description', None)
        return Movie(**movie_data)

    def match(self, json_data):
        '''Match json according to fields.

            Performs the following process:
                1. Validates json.
                2. Creates movie object.
                3. Performs matching.
                    3.1 Adds if the object is not found.

        :type json_data: dict
        :param json_data: movie data in json format

        :raises NotAcceptable: raises 406 error

        :rtype response: dict
        :returns: response status of the POST request
        '''
        # reset the response per request
        self.reset_response()

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

        # make input json a movie obect
        movie = self.create_movie(json_data)
        # search movie
        for movie_obj in self.storage:
            if movie_obj == movie:
                self.response['accepted'] = True
                movie_obj.increase_counter()
                self.response['counter'] = movie_obj.get_counter()

        # add as new movie
        if not self.response['accepted']:
            self.storage.append(movie)
            self.response['accepted'] = False
            self.response['counter'] = 0

        return self.response

    def reset_response(self):
        '''Reset the response result.
        '''
        self.response['counter'] = 0
        self.response['accepted'] = False
