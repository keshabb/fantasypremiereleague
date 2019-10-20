from fpl import FPL
import aiohttp


class TeamPerformance(object):

    async def get_teams_info(self):
        async with aiohttp.ClientSession() as session:
            fpl = FPL(session)
            teams = await fpl.get_teams(return_json=True)
            for team in teams:
                print(team)
        return teams
