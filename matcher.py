from error_request import NotAcceptable


class Matcher(object):
    def __init__(self):
        '''
            Matcher counter with object storage.
        '''
        self.response = {'accepted': False, 'counter': self.counter}
        self.counter = 0
        self.storage = []

    def match(self, json_data):
        '''
            Match json according to fields.

            :type json_data: dict
        '''
        # make sure is a dict
        if not isinstance(json_data, dict):
            raise NotAcceptable

        # if title and id are missing
        if not json_data.get('title', None) and \
                json_data.get('imdb_id', None):
            # TODO: change to object counter
            self.response['accepted'] = True
            self.response['counter'] = 0

        # if the storage is empty
        if not self.storage:
            self.storage.append(json_data)
        else:
            imdb_id = json_data.get('imdb_id', None)
            self.response['accepted'] = self.match_by_id(imdb_id)

        if not self.response['accepted']:
            raise NotAcceptable
        return self.response

    def match_by_id(self, imdb_id):
        '''
            Match data by id
        '''
        # TODO: change to be per object
        for json_entry in self.storage:
            imdb_id_db = json_entry.get('imdb_id', None)
            if imdb_id_db:
                if imdb_id_db == imdb_id:
                    self.counter += 1
                    self.storage.append(json_entry)
                    return True
        return False

    def match_by_title_year(self, title, year):
        '''
            Match data by title and year.
        '''
        pass

    def match_by_title_year_imdb_id(self, title, year, imdb_id):
        pass
    
