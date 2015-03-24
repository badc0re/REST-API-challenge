from error_request import NotAcceptable
from matcher import Matcher
import json
import web


urls = (
    '/decision', 'Api'
)
# make it global until application lives, see line 33
matcher = Matcher()


class Api(object):
    '''This is the API handling requests
       and uses Matcher to match data (json).
    
    :raises NotAcceptable: raises 406 error
        
    :rtype response: dict
    :returns: response status of the POST request 
    '''
    def POST(self):
        data = None
        try:
            data = web.data()
            json_data = json.loads(data)
            json_response_data = matcher.match(json_data)
            #TODO: this can be changed
            if not json_response_data['accepted']:
                raise NotAcceptable
            return json.dumps(json_response_data)
        except web.HTTPError:
            print 'Wrong request'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
