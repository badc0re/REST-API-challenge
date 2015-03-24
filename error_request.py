import web


class NotAcceptable(web.HTTPError):
    def __init__(self, message=None):
        message = "Not acceptable!"
        status = "406 Not Acceptable"
        headers = {'Content-Type': 'text/html'}
        web.HTTPError.__init__(self, status, headers, message)
