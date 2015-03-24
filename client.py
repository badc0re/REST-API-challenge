import requests
import json


class Client(object):
    def __init__(self):
        self.api_url = 'http://localhost:8080/decision'
        self.data_file = 'data/dataset.jl'

    def get_json_data(self):
        '''Loads test data from file.
        
        :rtype dict: dictionary data
        :returns: data from file
        '''
        with open(self.data_file) as json_file:
            return json.loads(json_file.read())

    def post_requests(self, json_post_data=None):
        '''Post requests to API, json POST requests.
            
        :type json_post_data: dict
        :param json_post_data: movie data in json format
        '''
        headers = {'Content-type': 'application/json',
                   'Accept': 'text/plain'}
        post_request = requests.post(self.api_url,
                                     data=json.dumps(json_post_data),
                                     headers=headers)
        #only print the response
        print post_request.text

    def make_request_to_api(self):
        '''Makes json post requests to server.
           Json data is from file.
        '''
        for json_post_data in self.get_json_data():
            self.post_requests(json_post_data=json_post_data)


if __name__ == "__main__":
    client = Client()
    client.make_request_to_api()
