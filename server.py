from matcher import Matcher
import json
import web


urls = (
    '/', 'Api'
)

matcher = Matcher()


class Api(object):
    '''
        This is the API handling requests
        and uses Matcher to match data (json).
    '''
    def POST(self):
        data = None
        try:
            data = web.data()
            json_data = json.loads(data)
            matcher.match(json_data)
        except web.HTTPError:
            print 'Wrong request'


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
