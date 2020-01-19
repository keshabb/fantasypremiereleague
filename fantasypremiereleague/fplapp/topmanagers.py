from fpl import FPL
import aiohttp
from django.conf import settings


class TopManagers(object):
    def __init__(self):
        self.overall_league_id = 314

    async def get_topmanagers(self):
        async with aiohttp.ClientSession() as session:
            fpl = FPL(session)
            await fpl.login(settings.USERNAME, settings.PASSWORD)
            resp = await fpl.get_classic_league(self.overall_league_id)
            league_info = await resp.get_standings()
        return league_info['results']
