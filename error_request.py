import web


class NotAcceptable(web.HTTPError):
    ''' 
        Extend HTTP status to 406.
        :returns: HTTP error with error status 406
    '''
    def __init__(self, message=None):
        message = "Not acceptable!"
        status = "406 Not Acceptable"
        headers = {'Content-Type': 'text/html'}
        web.HTTPError.__init__(self, status, headers, message)
