import http
import requests
import json

class GetRequester:
    url =  f"http://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    response = requests.get(url)

    def __init__(self, url):
        self.url = url


    def get_response_body(self):
        url =  f"http://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        response = requests.get(self.url)

        return response.content


    def load_json(self):
        url =  f"http://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        response = self.get_response_body()

        return json.loads(response.decode())
