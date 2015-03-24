import web


class NotAcceptable(web.HTTPError):
    ''' Error Status 406 '''

    def __init__(self, message=None):
        self.message = "not acceptable"
        status = "406 Not Acceptable"
        headers = {'Content-Type': 'text/html'}
        web.HTTPError.__init__(self, status, headers, message or self.message)
