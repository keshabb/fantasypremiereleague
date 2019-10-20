from django import template

register = template.Library()


@register.simple_tag()
def gameweek_filter(game_week, match_fixtures):
    return list(filter(lambda fixture: fixture['event'] == game_week, match_fixtures))

