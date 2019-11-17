import aiohttp
import asyncio
from fpl import FPL


class BotAI(object):
    def __init__(self):
        pass

    async def get_available_players(self):
        async with aiohttp.ClientSession() as session:
            fpl = FPL(session)
            players = await fpl.get_players(return_json=True)
            for player in players:
                player['roi'] = round((player['total_points'] / (player['now_cost'] / 10)), 2)
        return players

    async def get_teams(self):
        async with aiohttp.ClientSession() as session:
            fpl = FPL(session)
            teams = await fpl.get_teams(return_json=True)
            # TODO check return back on next game
            # if player['points_per_game'] != '0.0' and player['status'] in ('a', 'i') and player[
            #    'web_name'] == 'De Bruyne':
            # print(player)
            # print(player['web_name'], player['now_cost'], player['total_points'], player['bonus'], player['influence'], player['creativity'], player['threat'], player['ict_index'], player['status'])
            for team in teams:
                team['player_limit'] = 3
        return teams

    def build_team_by_roi(self, budget=100, count_limit=4, gk=2, df=5, md=5, fwd=3):
        players = asyncio.run(self.get_available_players())
        players_by_points = sorted(players, key=lambda i: i['total_points'], reverse=True)
        players_by_roi = sorted(players, key=lambda i: i['roi'], reverse=True)
        teams_info = asyncio.run(self.get_teams())
        money_team = []
        teams = dict()
        budget = budget
        # injured = players_by_status('injured')
        positions = {1: gk, 2: df, 3: md, 4: fwd}
        for team in teams_info:
            teams.update({team['code']: 3})
        for player in players_by_points:
            if len(money_team) < count_limit and player['status'] == 'a' and budget >= (player['now_cost'] / 10) and \
                    positions[player['element_type']] > 0 and teams[player['team_code']] > 0:
                team_name = list(filter(lambda player_team: player_team['code'] == player['team_code'], teams_info))[0]['short_name']
                player['team_name'] = team_name
                money_team.append(player)
                budget -= player['now_cost']/10
                positions[player['element_type']] = positions[player['element_type']] - 1
                teams[player['team_code']] = teams[player['team_code']] - 1
                print(f"Point player: {player['web_name']}")
            else:
                for player in players_by_roi:
                    if player not in money_team and budget >= (player['now_cost']/10) and positions[player['element_type']] > 0 and teams[player['team_code']] > 0:
                        team_name = list(filter(lambda player_team: player_team['code'] == player['team_code'], teams_info))[0]['short_name']
                        player['team_name'] = team_name
                        money_team.append(player)
                        budget -= player['now_cost']/10
                        positions[player['element_type']] = positions[player['element_type']] - 1
                        teams[player['team_code']] = teams[player['team_code']] - 1
                        print(f"RIO player: {player['web_name']}")
        final_team = [(item['web_name'], item['team_name'], item['element_type'], item['now_cost']/10) for item in money_team]
        total_points = sum([item['total_points'] for item in money_team])
        print('Remaining Budget: ' + str(round(budget, 2)))
        print('Your AI has picked the following team:')
        print('GK: '), print([(item[0], item[2]) for item in final_team if item[1] == 1])
        print('DF: '), print([(item[0], item[2]) for item in final_team if item[1] == 2])
        print('MD: '), print([(item[0], item[2]) for item in final_team if item[1] == 3])
        print('FWD: '), print([(item[0], item[2]) for item in final_team if item[1] == 4])
        print('Total Fantasy Points: ' + str(total_points))
        return final_team
