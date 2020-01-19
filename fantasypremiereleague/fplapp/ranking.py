import http.client as http_client
from django.conf import settings
import json


class Rank(object):
    def __init__(self):
        self.api_host = 'api.football-data.org'
        self.headers = {'X-Auth-Token': settings.API_KEY }

    def get_team_rank(self):

        conn = http_client.HTTPConnection(self.api_host)
        conn.request('GET', '/v2/competitions/PL/standings', None, self.headers)
        response = json.loads(conn.getresponse().read().decode())
        return response['standings'][0]['table']
