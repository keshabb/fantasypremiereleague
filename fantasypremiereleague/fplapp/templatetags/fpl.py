from django import template

register = template.Library()


@register.simple_tag()
def gameweek_filter(game_week, match_fixtures):
    return list(filter(lambda fixture: fixture['event'] == game_week, match_fixtures))


@register.simple_tag()
def team_short_name(team_id, teams):
    return teams[team_id]


@register.simple_tag()
def player_name(player_id, players):
    player_info = list(filter(lambda player: player['id'] == player_id, players))
    player_full_name = "{} {}".format(player_info[0]['first_name'], player_info[0]['second_name'])
    return player_full_name


@register.filter()
def price(cost):
    return cost / 10


@register.filter()
def position(element_type):
    element_types = {1: 'Goal Keeper', 2: 'Defender', 3: 'Midfielder', 4: 'Striker'}
    return element_types[element_type]


@register.filter()
def status(status_code):
    status_codes = {'d': 'Doubtful', 'i': 'Injured', 's': 'Suspended'}
    return status_codes[status_code]