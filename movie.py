from scorers.cosine import cosine_score


class Movie(object):
    '''Movie object created from json fields.
    '''
    def __init__(self, imdb_id, title, year, description):
        self.counter = 1
        self.imdb_id = imdb_id
        self.title = title
        self.year = year
        self.description = description

    def get_counter(self):
        '''Returns counter current value.
        '''
        return self.counter

    def increase_counter(self):
        '''Increase the value of the counter.
        '''
        self.counter += 1

    def __eq__(self, other_obj):
        if (other_obj.imdb_id and self.imdb_id) and \
                (other_obj.imdb_id == self.imdb_id):
            # match_by_id
            return True
        elif (other_obj.title and self.year) and \
                (other_obj.year == self.year):
            # match by title and year
            if cosine_score(other_obj.title, self.title) > 0.90:
                # the treshold can be increased
                return True
        elif other_obj.description and self.year:
            # match by year and description
            if cosine_score(other_obj.description, self.description) > 0.90:
                # the treshold can be increased
                return True
        return False
