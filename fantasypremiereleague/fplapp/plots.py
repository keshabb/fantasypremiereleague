import datetime
import glob
import logging
import os
import asyncio

from . import fdr
import numpy as np
from operator import itemgetter
import plotly.graph_objects as go
from plotly.offline import plot
from plotly.subplots import make_subplots

logger = logging.getLogger(__name__)


def get_defense_team(strength_type):
    obj = fdr.FDR()
    data = asyncio.run(obj.fdr())
    defense_data = [{'Team': key, 'fdr': (value['defender']['H'] + value['defender']['A'])/2,
                     'fdr_home': value['defender']['H'],
                     'fdr_away': value['defender']['A']} for key, value in data.items()]
    if strength_type == "best":
        defense_team = sorted(defense_data, key=itemgetter('fdr'), reverse=True)[:7]
    elif strength_type == "worst":
        defense_team = sorted(defense_data, key=itemgetter('fdr'))[:7]
    else:
        # TODO exception handling
        print("Invalid strength type")
    defense_teams = []
    fdr_home = []
    fdr_away = []
    fdr_rank = []
    for item in defense_team:
        defense_teams.append(item['Team'])
        fdr_rank.append(item['fdr'])
        fdr_home.append(item['fdr_home'])
        fdr_away.append(item['fdr_away'])
    return defense_teams, fdr_rank, fdr_home, fdr_away


def get_offensive_team(strength_type):
    obj = fdr.FDR()
    data = asyncio.run(obj.fdr())
    offensive_data = [{'Team': key, 'fdr': (value['forward']['H'] + value['forward']['A'])/2,
                       'fdr_home': value['forward']['H'],
                       'fdr_away': value['forward']['A']} for key, value in data.items()]
    if strength_type == "best":
        ofensive_team = sorted(offensive_data, key=itemgetter('fdr'), reverse=True)[:7]
    elif strength_type == "worst":
        ofensive_team = sorted(offensive_data, key=itemgetter('fdr'))[:7]
    else:
        # TODO exception handling
        print("Invalid strength type")
    offensive_teams = []
    fdr_rank = []
    fdr_home = []
    fdr_away = []
    for item in ofensive_team:
        offensive_teams.append(item['Team'])
        fdr_rank.append(item['fdr'])
        fdr_home.append(item['fdr_home'])
        fdr_away.append(item['fdr_away'])
    return offensive_teams, fdr_rank, fdr_home, fdr_away


def get_midfielder_team(strength_type):
    obj = fdr.FDR()
    data = asyncio.run(obj.fdr())
    midfielder_data = [{'Team': key, 'fdr': (value['midfielder']['H'] + value['midfielder']['A'])/2,
                        'fdr_home': value['midfielder']['H'],
                        'fdr_away': value['midfielder']['A']} for key, value in data.items()]
    if strength_type == "best":
        midfielder_team = sorted(midfielder_data, key=itemgetter('fdr'), reverse=True)[:7]
    elif strength_type == "worst":
        midfielder_team = sorted(midfielder_data, key=itemgetter('fdr'))[:7]
    else:
        # TODO exception handling
        print("Invalid strength type")
    midfielder_teams = []
    fdr_rank = []
    fdr_home = []
    fdr_away = []
    for item in midfielder_team:
        midfielder_teams.append(item['Team'])
        fdr_rank.append(item['fdr'])
        fdr_home.append(item['fdr_home'])
        fdr_away.append(item['fdr_away'])
    return midfielder_teams, fdr_rank, fdr_home, fdr_away


def get_goalkeeper_team(strength_type):
    obj = fdr.FDR()
    data = asyncio.run(obj.fdr())
    goalkeeper_data = [{'Team': key, 'fdr': (value['goalkeeper']['H'] + value['goalkeeper']['A'])/2,
                        'fdr_home': value['goalkeeper']['H'],
                        'fdr_away': value['goalkeeper']['A']} for key, value in data.items()]
    if strength_type == "best":
        goalkeeper_team = sorted(goalkeeper_data, key=itemgetter('fdr'), reverse=True)[:7]
    elif strength_type == "worst":
        goalkeeper_team = sorted(goalkeeper_data, key=itemgetter('fdr'))[:7]
    else:
        # TODO exception handling
        print("Invalid strength type")
    goalkeeper_teams = []
    fdr_rank = []
    fdr_home = []
    fdr_away = []
    for item in goalkeeper_team:
        goalkeeper_teams.append(item['Team'])
        fdr_rank.append(item['fdr'])
        fdr_home.append(item['fdr_home'])
        fdr_away.append(item['fdr_away'])
    return goalkeeper_teams, fdr_rank, fdr_home, fdr_away


def team_strength_plot():
    obj = fdr.FDR()
    data = asyncio.run(obj.fdr())
    team_strength_data = [{'Team': key, 'fdr_avg': (value['all']['H'] + value['all']['A'])/2,
                           'fdr_home': value['all']['H'], 'fdr_away': value['all']['A']} for key, value in data.items()]
    sorted_team_strength_data = sorted(team_strength_data, key=itemgetter('fdr_avg'), reverse=True)
    best_defense_team, best_def_fdr_rank, fdr_def_best_home, fdr_def_best_away = get_defense_team("best")
    worst_defense_team, worst_def_fdr_rank, fdr_def_worst_home, fdr_def_worst_away = get_defense_team("worst")
    print(f"Worst Def: {worst_defense_team}")
    best_offense_team, best_off_fdr_rank, fdr_off_best_home, fdr_off_best_away = get_offensive_team("best")
    print(f"Best Off: {best_offense_team} {best_off_fdr_rank}")
    print(f"Best Off: {best_offense_team} {fdr_off_best_home}")
    worst_offense_team, worst_off_fdr_rank, fdr_off_worst_home, fdr_off_worst_away = get_offensive_team("worst")
    best_mid_team, best_mid_fdr_rank, fdr_mid_best_home, fdr_mid_best_away = get_midfielder_team("best")
    worst_mid_team, worst_mid_fdr_rank, fdr_mid_worst_home, fdr_mid_worst_away = get_midfielder_team("worst")
    best_gk_team, best_gk_fdr_rank,  fdr_gk_best_home, fdr_gk_best_away = get_goalkeeper_team("best")
    worst_gk_team, worst_gk_fdr_rank,  fdr_gk_worst_home, fdr_gk_worst_away = get_goalkeeper_team("worst")
    teams = []
    overall_team_strength = []
    team_strength_home = []
    team_strength_away = []
    for item in sorted_team_strength_data:
        teams.append(item['Team'])
        overall_team_strength.append(item['fdr_avg'])
        team_strength_home.append(item['fdr_home'])
        team_strength_away.append(item['fdr_away'])
    fig = make_subplots(
        rows=5, cols=2,
        specs=[[{"colspan": 2}, None],
               [{}, {}],
               [{}, {}],
               [{}, {}],
               [{}, {}]],
        subplot_titles=("Overall Team Strength",
                        "Best 7 Defense", "Worst 7 Defense",
                        "Best 7 Offense", "Worst 7 Offense",
                        "Best 7 Midfielder", "Worst 7 Midfielder",
                        "Best 7 Goalkeeper", "Worst 7 Goalkeeper"))
    avg_team_strength = go.Bar(
        name="Overall Team Strength",
        x=teams,
        y=overall_team_strength
    )
    team_home_strength = go.Bar(
        name="Home",
        x=teams,
        y=team_strength_home
    )
    team_away_strength = go.Bar(
        name="Away",
        x=teams,
        y=team_strength_away
    )
    best_defensive_team = go.Bar(
        name="Best Defense",
        x=best_defense_team,
        y=best_def_fdr_rank
    )
    best_defensive_team_home = go.Bar(
        name="Home",
        x=best_defense_team,
        y=fdr_def_best_home
    )
    best_defensive_team_away = go.Bar(
        name="Away",
        x=best_defense_team,
        y=fdr_def_best_away
    )
    worst_defensive_team = go.Bar(
        name="Worst Defense",
        x=worst_defense_team,
        y=worst_def_fdr_rank
    )
    worst_defensive_home = go.Bar(
        name="Home",
        x=worst_defense_team,
        y=fdr_def_worst_home
    )
    worst_defensive_away = go.Bar(
        name="Away",
        x=worst_defense_team,
        y=fdr_def_worst_away
    )
    best_offensive_team = go.Bar(
        name="Best Offense",
        x=best_offense_team,
        y=best_off_fdr_rank
    )
    best_offensive_home = go.Bar(
        name="Home",
        x=best_offense_team,
        y=fdr_off_best_home
    )
    best_offensive_away = go.Bar(
        name="Away",
        x=best_offense_team,
        y=fdr_off_best_away
    )
    worst_offensive_team = go.Bar(
        name="Worst 7 Offense",
        x=worst_offense_team,
        y=worst_off_fdr_rank
    )
    worst_offensive_home = go.Bar(
        name="Home",
        x=worst_offense_team,
        y=fdr_off_worst_home
    )
    worst_offensive_away = go.Bar(
        name="Away",
        x=worst_offense_team,
        y=fdr_off_worst_away
    )
    best_midfielder_team = go.Bar(
        name="Best 7 Midfielder",
        x=best_mid_team,
        y=best_mid_fdr_rank
    )
    best_midfielder_home = go.Bar(
        name="Home",
        x=best_mid_team,
        y=fdr_mid_best_home
    )
    best_midfielder_away = go.Bar(
        name="Away",
        x=best_mid_team,
        y=fdr_mid_best_away
    )
    worst_midfielder_team = go.Bar(
        name="Worst 7 Midfielder",
        x=worst_mid_team,
        y=worst_mid_fdr_rank
    )
    worst_midfielder_home = go.Bar(
        name="Home",
        x=worst_mid_team,
        y=fdr_mid_worst_home
    )
    worst_midfielder_away = go.Bar(
        name="Away",
        x=worst_mid_team,
        y=fdr_mid_worst_away
    )
    best_goalkeeper_team = go.Bar(
        name="Best 7 Goalkeeper",
        x=best_gk_team,
        y=best_gk_fdr_rank
    )
    best_goalkeeper_home = go.Bar(
        name="Home",
        x=best_gk_team,
        y=fdr_gk_best_home
    )
    best_goalkeeper_away = go.Bar(
        name="Away",
        x=best_gk_team,
        y=fdr_gk_best_away
    )
    worst_goalkeeper_team = go.Bar(
        name="Worst 7 Goalkeeper",
        x=worst_gk_team,
        y=worst_gk_fdr_rank
    )
    worst_goalkeeper_home = go.Bar(
        name="Home",
        x=worst_gk_team,
        y=fdr_gk_worst_home
    )
    worst_goalkeeper_away = go.Bar(
        name="Away",
        x=worst_gk_team,
        y=fdr_gk_worst_away
    )

    fig.add_trace(avg_team_strength, row=1, col=1)
    fig.add_trace(team_home_strength, row=1, col=1)
    fig.add_trace(team_away_strength, row=1, col=1)
    fig.add_trace(best_defensive_team, row=2, col=1)
    fig.add_trace(best_defensive_team_home, row=2, col=1)
    fig.add_trace(best_defensive_team_away, row=2, col=1)
    fig.add_trace(worst_defensive_team, row=2, col=2)
    fig.add_trace(worst_defensive_home, row=2, col=2)
    fig.add_trace(worst_defensive_away, row=2, col=2)
    fig.add_trace(best_offensive_team, row=3, col=1)
    fig.add_trace(best_offensive_home, row=3, col=1)
    fig.add_trace(best_offensive_away, row=3, col=1)
    fig.add_trace(worst_offensive_team, row=3, col=2)
    fig.add_trace(worst_offensive_home, row=3, col=2)
    fig.add_trace(worst_offensive_away, row=3, col=2)
    fig.add_trace(best_midfielder_team, row=4, col=1)
    fig.add_trace(best_midfielder_home, row=4, col=1)
    fig.add_trace(best_midfielder_away, row=4, col=1)
    fig.add_trace(worst_midfielder_team, row=4, col=2)
    fig.add_trace(worst_midfielder_home, row=4, col=2)
    fig.add_trace(worst_midfielder_away, row=4, col=2)
    fig.add_trace(best_goalkeeper_team, row=5, col=1)
    fig.add_trace(best_goalkeeper_home, row=5, col=1)
    fig.add_trace(best_goalkeeper_away, row=5, col=1)
    fig.add_trace(worst_goalkeeper_team, row=5, col=2)
    fig.add_trace(worst_goalkeeper_home, row=5, col=2)
    fig.add_trace(worst_goalkeeper_away, row=5, col=2)
    layout = go.Layout(
        title="Team Strength",
        #autosize=True,
        #width=900,
        #height=1900,

        xaxis=dict(
            autorange=True,
        ),
        yaxis=dict(
            autorange=True
        )
    )
    fig = go.Figure(data=fig, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False, image_height=1900)
    logger.info("Plotting number of points {}.".format(len(teams)))
    return plot_div
