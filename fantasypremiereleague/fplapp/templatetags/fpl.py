from django import template
from fplapp.fixtures import Fixtures
import asyncio

register = template.Library()


@register.simple_tag()
def gameweek_filter(game_week, match_fixtures):
    return list(filter(lambda fixture: fixture['event'] == game_week, match_fixtures))

@register.simple_tag()
def team_short_name(team_id, teams):
    return teams[team_id]