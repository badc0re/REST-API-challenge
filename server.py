import web


urls = (
    '/', 'api'
)


class NotAcceptable(web.HTTPError):
    ''' Error Status 406 '''

    def __init__(self, message=None):
        self.message = "not acceptable"
        status = "406 Not Acceptable"
        headers = {'Content-Type': 'text/html'}
        web.HTTPError.__init__(self, status, headers, message or self.message)


class api:
    def POST(self):
        data = None
        try:
            data = web.data()
            print data
            #raise NotAcceptable
        except web.HTTPError:
            print 'Wrong request'


if __name__ == "__main__":
    app = web.application(urls,
                          globals())
    app.run()
