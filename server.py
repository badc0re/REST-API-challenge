import web


urls = (
    '/', 'Api'
)


class NotAcceptable(web.HTTPError):
    ''' Error Status 406 '''

    def __init__(self, message=None):
        self.message = "not acceptable"
        status = "406 Not Acceptable"
        headers = {'Content-Type': 'text/html'}
        web.HTTPError.__init__(self, status, headers, message or self.message)


class Matcher(object):
    def __init__(self):
        self.counter = 0
        self.storage = []

    def match(self, json_data):
        print json_data
        print 'matcher'


class Api(object):
    '''
        This is the API handling requests
        and uses Matcher to match data (json).
    '''
    def __init__(self):
        self.matcher = Matcher()

    def POST(self):
        data = None
        try:
            data = web.data()
            self.matcher.match(data)
            #raise NotAcceptable
        except web.HTTPError:
            print 'Wrong request'


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
