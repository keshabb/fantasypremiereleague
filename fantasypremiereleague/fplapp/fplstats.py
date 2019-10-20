import requests


class FPLStats(object):
    def __init__(self):
        self.api_url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

    def get_events_info(self):
        resp = requests.get(self.api_url)
        events_info = resp.json()['events']
        return events_info
