from fpl import FPL
import aiohttp
import asyncio


class Fixtures(object):

    async def match_fixtures(self):
        async with aiohttp.ClientSession() as session:
            fpl = FPL(session)
            fixtures = await fpl.get_fixtures(return_json=True)
        return fixtures

    async def get_team_short_name(self):
        async with aiohttp.ClientSession() as session:
            fpl = FPL(session)
            result = await fpl.get_teams(return_json=True)
            teams = {}
            for team in result:
                teams.update({team['id']: team['short_name']})
            print(teams)
        return teams
