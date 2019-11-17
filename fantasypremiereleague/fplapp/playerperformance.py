from fpl import FPL
import aiohttp


class PlayerPerformance:

    async def get_players_info(self, player_ids=None):
        async with aiohttp.ClientSession() as session:
            fpl = FPL(session)
            players = await fpl.get_players(player_ids, return_json=True)
        return players
