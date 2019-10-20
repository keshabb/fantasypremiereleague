from fpl import FPL
import aiohttp


class Transfer(object):

    async def get_players_info(self):
        async with aiohttp.ClientSession() as session:
            fpl = FPL(session)
            players_info = await fpl.get_players(return_json=True)
        return players_info
