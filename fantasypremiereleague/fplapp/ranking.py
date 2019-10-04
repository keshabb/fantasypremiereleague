import http.client as http_client
import json


class Rank(object):
    def __init__(self):
        self.api_host = 'api.football-data.org'
        self.headers = {'X-Auth-Token': ''}

    def get_team_rank(self):
        conn = http_client.HTTPConnection(self.api_host)
        print("I am making request")
        conn.request('GET', '/v2/competitions/PL/standings', None, self.headers)
        response = json.loads(conn.getresponse().read().decode())
        return response['standings'][0]['table']
