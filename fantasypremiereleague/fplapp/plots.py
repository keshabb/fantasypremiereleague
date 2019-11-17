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
    defense_data = [{'Team': key, 'fdr': (value['defender']['H'] + value['defender']['A'])/2} for key, value in data.items()]
    if strength_type == "best":
        defense_team = sorted(defense_data, key=itemgetter('fdr'), reverse=True)[:7]
    elif strength_type == "worst":
        defense_team = sorted(defense_data, key=itemgetter('fdr'))[:7]
    else:
        # TODO exception handling
        print("Invalid strength type")
    defense_teams = []
    fdr_rank = []
    for item in defense_team:
        defense_teams.append(item['Team'])
        fdr_rank.append(item['fdr'])
    return defense_teams, fdr_rank


def get_offensive_team(strength_type):
    obj = fdr.FDR()
    data = asyncio.run(obj.fdr())
    offensive_data = [{'Team': key, 'fdr': (value['forward']['H'] + value['forward']['A'])/2} for key, value in data.items()]
    if strength_type == "best":
        ofensive_team = sorted(offensive_data, key=itemgetter('fdr'), reverse=True)[:7]
    elif strength_type == "worst":
        ofensive_team = sorted(offensive_data, key=itemgetter('fdr'))[:7]
    else:
        # TODO exception handling
        print("Invalid strength type")
    offensive_teams = []
    fdr_rank = []
    for item in ofensive_team:
        offensive_teams.append(item['Team'])
        fdr_rank.append(item['fdr'])
    return offensive_teams, fdr_rank


def get_midfielder_team(strength_type):
    obj = fdr.FDR()
    data = asyncio.run(obj.fdr())
    midfielder_data = [{'Team': key, 'fdr': (value['midfielder']['H'] + value['midfielder']['A'])/2} for key, value in data.items()]
    if strength_type == "best":
        midfielder_team = sorted(midfielder_data, key=itemgetter('fdr'), reverse=True)[:7]
    elif strength_type == "worst":
        midfielder_team = sorted(midfielder_data, key=itemgetter('fdr'))[:7]
    else:
        # TODO exception handling
        print("Invalid strength type")
    midfielder_teams = []
    fdr_rank = []
    for item in midfielder_team:
        midfielder_teams.append(item['Team'])
        fdr_rank.append(item['fdr'])
    return midfielder_teams, fdr_rank


def get_goalkeeper_team(strength_type):
    obj = fdr.FDR()
    data = asyncio.run(obj.fdr())
    goalkeeper_data = [{'Team': key, 'fdr': (value['goalkeeper']['H'] + value['goalkeeper']['A'])/2} for key, value in data.items()]
    if strength_type == "best":
        goalkeeper_team = sorted(goalkeeper_data, key=itemgetter('fdr'), reverse=True)[:7]
    elif strength_type == "worst":
        goalkeeper_team = sorted(goalkeeper_data, key=itemgetter('fdr'))[:7]
    else:
        # TODO exception handling
        print("Invalid strength type")
    goalkeeper_teams = []
    fdr_rank = []
    for item in goalkeeper_team:
        goalkeeper_teams.append(item['Team'])
        fdr_rank.append(item['fdr'])
    return goalkeeper_teams, fdr_rank


def team_strength_plot():
    obj = fdr.FDR()
    data = asyncio.run(obj.fdr())
    team_strength_data = [{'Team': key, 'fdr': (value['all']['H'] + value['all']['A'])/2} for key, value in data.items()]
    sorted_team_strength_data = sorted(team_strength_data, key=itemgetter('fdr'), reverse=True)
    best_defense_team, best_fdr_rank = get_defense_team("best")
    worst_defense_team, worst_fdr_rank = get_defense_team("worst")
    best_offense_team, best_fdr_rank = get_offensive_team("best")
    worst_offense_team, worst_fdr_rank = get_offensive_team("worst")
    best_midfielder_team, best_fdr_rank = get_midfielder_team("best")
    worst_midfielder_team, worst_fdr_rank = get_midfielder_team("worst")
    best_goalkeeper_team, best_fdr_rank = get_goalkeeper_team("best")
    worst_goalkeeper_team, worst_fdr_rank = get_goalkeeper_team("worst")
    teams = []
    overall_team_strength = []
    for item in sorted_team_strength_data:
        teams.append(item['Team'])
        overall_team_strength.append(item['fdr'])
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
    trace1 = go.Bar(
        name="Overall Team Strength",
        x=teams,
        y=overall_team_strength
    )
    trace2 = go.Bar(
        name="Best 7 Defense",
        x=best_defense_team,
        y=best_fdr_rank
    )
    trace3 = go.Bar(
        name="Worst 7 Defense",
        x=worst_defense_team,
        y=worst_fdr_rank
    )
    trace4 = go.Bar(
        name="Best 7 Offense",
        x=best_offense_team,
        y=best_fdr_rank
    )
    trace5 = go.Bar(
        name="Worst 7 Offense",
        x=worst_offense_team,
        y=worst_fdr_rank
    )
    trace6 = go.Bar(
        name="Best 7 Midfielder",
        x=best_midfielder_team,
        y=best_fdr_rank
    )
    trace7 = go.Bar(
        name="Worst 7 Midfielder",
        x=worst_midfielder_team,
        y=worst_fdr_rank
    )
    trace8 = go.Bar(
        name="Best 7 Goalkeeper",
        x=best_goalkeeper_team,
        y=best_fdr_rank
    )
    trace9 = go.Bar(
        name="Worst 7 Goalkeeper",
        x=worst_goalkeeper_team,
        y=worst_fdr_rank
    )
    fig.add_trace(trace1, row=1, col=1)
    fig.add_trace(trace2, row=2, col=1)
    fig.add_trace(trace3, row=2, col=2)
    fig.add_trace(trace4, row=3, col=1)
    fig.add_trace(trace5, row=3, col=2)
    fig.add_trace(trace6, row=4, col=1)
    fig.add_trace(trace7, row=4, col=2)
    fig.add_trace(trace8, row=5, col=1)
    fig.add_trace(trace9, row=5, col=2)
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
    plot_div = plot(fig, output_type='div', include_plotlyjs=False, image_height=900)
    logger.info("Plotting number of points {}.".format(len(teams)))
    return plot_div
